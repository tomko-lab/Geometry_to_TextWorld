import geojson
from geojson import Polygon
from shapely.geometry import *
import matplotlib.pylab as p
import math
import numpy as np
from scipy.spatial import Delaunay
import random
import skgeom as sg
from parameters import Parameter

def all_vertices_extraction(unit_coor_list):
    all_vertices = []
    if len(unit_coor_list[0]) >2:
        for u in unit_coor_list:
            for v in u:
                all_vertices.append(v)
    else:
        for u in unit_coor_list:
            all_vertices.append(u)

    return all_vertices

def to_coordinates(string_coordinates):
  return [float(val) for val in string_coordinates.replace('[', '').replace(']', '').split(', ')]

def data_collection():

    with open(Parameter.DATASET_DIRECTORY + Parameter.ENV) as f:
        unit = geojson.load(f)

    with open(Parameter.DATASET_DIRECTORY + Parameter.DOORS) as f:
        doors = geojson.load(f)


    door = []
    for d in range(0, len(doors['features'])):
        door.append(doors['features'][d].geometry.coordinates)

    with open(Parameter.DATASET_DIRECTORY + Parameter.LANDMARKS) as f:
        landmark = geojson.load(f)

    landmarks = {}
    for d in range(0, len(landmark['features'])):
        landmarks[d] = {}
        landmarks[d]["geometry"] = landmark['features'][d].geometry.coordinates
        landmarks[d]["description"] = landmark['features'][d]["properties"]['description']

    """"This is the multipolygon of the main unit including the holes."""
    unit_coor_multipolygon = {}
    bounds_unit = {}
    bb_unit ={}
    unit_coor_list = {}
    all_vertices = {}
    unit_main_coor = {}
    for i in range(0, len(unit['features'])):
        unit_coor_multipolygon[i] = shape(unit['features'][i].geometry)
        bounds_unit[i] = unit_coor_multipolygon[i].bounds
        bb_unit[i] = [[bounds_unit[i][0], bounds_unit[i][1]], [bounds_unit[i][2], bounds_unit[i][1]], [bounds_unit[i][2], bounds_unit[i][3]],
                   [bounds_unit[i][0], bounds_unit[i][3]], [bounds_unit[i][0], bounds_unit[i][1]]]
        unit_coor_list[i] = unit['features'][i].geometry.coordinates[0]
        all_vertices[i] = all_vertices_extraction(unit_coor_list[i])
        unit_main_coor[i] = unit_coor_list[i]
        """The main polygon should ve ccw"""
        if not LinearRing(unit_main_coor[i]).is_ccw:
            unit_main_coor[i].reverse()

    return bb_unit, unit_main_coor, door, landmarks

def edge(vertices):
    polygon_edges = []
    for j in range(0, len(vertices) - 1):
        polygon_edges.append([vertices[j], vertices[j + 1]])

    return polygon_edges

def intersection(line1, line2):
    x_diff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    y_diff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def determinant(a, b):
        return a[0] * b[1] - a[1] * b[0]

    divergence = determinant(x_diff, y_diff)
    if divergence == 0:
        x = None
        y = None
    else:
        d = (determinant(*line1), determinant(*line2))
        x = determinant(d, x_diff) / divergence
        y = determinant(d, y_diff) / divergence
    return x, y

def visibility_decomposition(vertices, bb_unit, epsilon):
    """ Visibility decomposition introduced by chen 1998 """
    unit_coor_multipolygon = Polygon(vertices)
    global critical_point
    bb_edges = edge(bb_unit)
    critical_points = []
    virtual_lines = []
    for v in range(0,len(vertices)-1):
        for w in range(v+1, len(vertices)):
            if vertices[v] != vertices[w]:
                ray = [vertices[v], vertices[w]]
                if LineString(ray).within(unit_coor_multipolygon.buffer(epsilon)):
                    max_line =[]
                    max_line_point = []
                    for e in bb_edges:
                        [x, y] = [intersection(ray, e)[0], intersection(ray, e)[1]]
                        if [x, y] == [None, None]:
                            continue
                        if Point([x,y]).within(LineString(e).buffer(epsilon)):
                            max_line.append([x,y])
                            max_line_point.append(Point([x,y]))
                    max_line = LineString([min(max_line), max(max_line)])


                    main_intersections = unit_coor_multipolygon.intersection(max_line)
                    if not main_intersections.is_empty:
                        intersections = []
                        if main_intersections.geom_type == 'GeometryCollection' or main_intersections.geom_type == 'MultiLineString':
                            for inter in main_intersections:
                                """"Since the answer might be a GEOMETRYCOLLECTION,
                                 here, we are extracting the intersection points."""
                                if inter.geom_type == 'LineString':
                                    if Point([inter.xy[0][0],inter.xy[1][0]]).disjoint(Point(vertices[v]).buffer(epsilon)) and Point([inter.xy[0][0],inter.xy[1][0]]).disjoint(Point(vertices[w]).buffer(epsilon)) :
                                        intersections.append(Point([inter.xy[0][0],inter.xy[1][0]]))
                                    if Point([inter.xy[0][1],inter.xy[1][1]]).disjoint(Point(vertices[v]).buffer(epsilon)) and Point([inter.xy[0][1],inter.xy[1][1]]).disjoint(Point(vertices[w]).buffer(epsilon)):

                                        intersections.append(Point([inter.xy[0][1],inter.xy[1][1]]))
                                else:
                                    if not inter.within(Point(vertices[v]).buffer(epsilon)) and not inter.within(Point(vertices[w]).buffer(epsilon)):
                                        intersections.append(inter)
                        if intersections:
                            for inter in intersections:
                                check_line = LineString([Point(vertices[v]),inter])
                                if check_line.within(unit_coor_multipolygon.buffer(epsilon)):
                                    critical_points.append(inter)
                                    check_vertex = False
                                    for vp in vertices:
                                        if inter.within(Point(vp).buffer(epsilon)):
                                            check_vertex = True
                                    if check_vertex == False:
                                        virtual_lines.append(LineString((Point(vertices[w]),inter)))
    x_unit, y_unit = Polygon(vertices).exterior.xy
    critical_points_list = [[point.xy[0][0], point.xy[1][0]] for point in critical_points]

    points = np.array(critical_points_list)

    tri = Delaunay(points)
    triangles_list = list(tri.vertices)
    triangles_coor_list = []
    for triangle in triangles_list:
        triangle_coor = []
        for p_ind in triangle:
            triangle_coor.append([points[p_ind][0],points[p_ind][1]])

        if Polygon(triangle_coor).within(Polygon(vertices)):
            triangles_coor_list.append(Polygon(triangle_coor))
    # p.triplot(points[:, 0], points[:, 1], tri.simplices)

    # for triangle in triangles_coor_list:
    #     x_triangle, y_triangle = triangle.exterior.xy
    #     p.plot(x_triangle, y_triangle)
    """For decomposition"""
    vir_multi = MultiLineString(virtual_lines)
    vir_multi_buffer = vir_multi.buffer(epsilon)
    regions = Polygon(vertices).difference(vir_multi_buffer)



    # for l in virtual_lines:
    #     p.plot(*l.xy)
    p.plot(x_unit, y_unit)
    for geom in regions:
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        x_geom, y_geom= geom.exterior.xy
        p.plot(x_geom, y_geom, c = color)
    xs = [point.x for point in critical_points]
    ys = [point.y for point in critical_points]
    p.scatter(xs, ys)
    p.show()

    return critical_points

def cardinal_direction(angle_degree):

    if (angle_degree >= 0 and angle_degree < 22.5) or (angle_degree > 337.5 and angle_degree <= 360):
        cardinal_dir = "N"
    elif (angle_degree >= 22.5 and angle_degree < 67.5):
        cardinal_dir = "NW"
    elif (angle_degree >= 67.5 and angle_degree < 112.5):
        cardinal_dir = "W"
    elif (angle_degree >= 112.5 and angle_degree < 157.5):
        cardinal_dir = "SW"
    elif (angle_degree >= 157.5 and angle_degree < 202.5):
        cardinal_dir = "S"
    elif (angle_degree >= 202.5 and angle_degree < 247.5):
        cardinal_dir = "SE"
    elif (angle_degree >= 247.5 and angle_degree < 292.5):
        cardinal_dir = "E"
    elif (angle_degree >= 292.5 and angle_degree < 337.5):

        cardinal_dir = "NE"

    return cardinal_dir

def decision_points_decomposition (env_coor_list):
    """"This is for each polygon..."""

    del env_coor_list[-1]
    polygon = sg.Polygon(env_coor_list)

    """"Make the skeleton"""
    skeleton = sg.skeleton.create_interior_straight_skeleton(polygon)
    # draw(polygon)

    """Extract the vertices of the skeleton"""
    env_coor_list.append(env_coor_list[0])
    env_pol = Polygon(env_coor_list)

    skel_vertices = {}
    for v in skeleton.vertices:
        if Point([v.point.x(), v.point.y()]).within(env_pol) and [v.point.x(), v.point.y()] not in skel_vertices.values():
            skel_vertices[v.id] = [v.point.x(), v.point.y()]


    regions = {}
    for h in skeleton.halfedges:
        if [h.vertex.point.x(), h.vertex.point.y()] in skel_vertices.values():
            if [h.next.vertex.point.x(), h.next.vertex.point.y()] not in env_coor_list and [h.next.vertex.point.x(), h.next.vertex.point.y()] not in regions.values():
                if [h.vertex.point.x(), h.vertex.point.y()] != [h.next.vertex.point.x(), h.next.vertex.point.y()]:

                    regions[str(h.vertex.id)+str(h.next.vertex.id)] = [[h.vertex.point.x(), h.vertex.point.y()], [h.next.vertex.point.x(), h.next.vertex.point.y()]]

    """"finding the start point"""
    chain = []
    for key, value in regions.items():
        if value[0] == min(skel_vertices.values()):
            chain.append(value)
    """creating the nodes: each element in the chain is the characteristic of each node"""
    counter = 0
    while counter < len(regions)/2:
        for key, value in regions.items():
            if value[0] == chain[counter][1] and value[1] != chain[counter][0]:
                chain.append(value)
        counter += 1

    nodes = {}
    for n in chain:
        if nodes.get(str(n[0])) == None:
            nodes[str(n[0])] = {}
        for next in chain:
            if n[0] == next[0]:
                if nodes.get(str(next[1])) == None:
                    nodes[str(next[1])] = {}
                first = np.array(n[0])
                second = np.array([n[0][0],n[0][1]+100])
                third = np.array(next[1])
                fs = second - first
                st = third - first

                angle_degree = math.degrees(
                    math.atan2(st[1], st[0]) - math.atan2(fs[1], fs[0]))
                oppo_angle_degree = angle_degree - 180
                if angle_degree < 0:
                    angle_degree = angle_degree + 360
                if oppo_angle_degree < 0:
                    oppo_angle_degree = oppo_angle_degree + 360

                cardinal_dir = cardinal_direction(angle_degree)
                oppo_cardinal_dir = cardinal_direction(oppo_angle_degree)
                nodes[str(n[0])][str(next[1])] = cardinal_dir
                nodes[str(next[1])][str(n[0])] = oppo_cardinal_dir
    return nodes

def landmarks_parent_area(env_coord_list, nodes, landmarks):
    for key_lm,value_lm in landmarks.items():
        value_lm['visible_areas'] = []
        value_lm['parent_area'] = ''
        for key_room, value_room in env_coord_list.items():
            if Point(value_lm['geometry']).within(Polygon(value_room)) or Point(value_lm['geometry']).touches(Polygon(value_room)) :
                lm_room = Polygon(value_room)
                nodes_room = []
                for key_node, value_node in nodes[key_room].items():
                    nodes_room.append(key_node)


        for area in nodes_room:
            ray = [value_lm['geometry'], to_coordinates(area)]
            if LineString(ray).relate_pattern(lm_room,'1FF0*F212'):
                value_lm['visible_areas'].append(area)

        distances = []
        for vis in value_lm['visible_areas']:
            distances.append(Point(value_lm['geometry']).distance(Point(to_coordinates(vis))))

        value_lm['parent_area'] = value_lm['visible_areas'][distances.index(min(distances))]


    return landmarks

def doors_parent_area(env_coord_list, nodes, doors):
    door_parent = {}
    for door in doors:
        door_parent[doors.index(door)] = {}
        door_parent[doors.index(door)]['geometry'] = door
        door_parent[doors.index(door)]['visible_areas'] = []
        door_parent[doors.index(door)]['parent_room'] = []
        door_parent[doors.index(door)]['parent_area'] = []
        door_rooms = {}
        for key_room, value_room in env_coord_list.items():
            if Point(door).touches(Polygon(value_room)) or \
                    Point(door).distance(Polygon(value_room)) < Parameter.MIN_DISTANCE:
                door_parent[doors.index(door)]['parent_room'].append(key_room)
                door_rooms[key_room] = {}
                door_rooms[key_room]['room'] = Polygon(value_room)
                nodes_room = []
                nodes_room_name = []
                for key_node, value_node in nodes[key_room].items():
                    nodes_room.append(to_coordinates(key_node))
                    nodes_room_name.append(key_node)
                door_rooms[key_room]['areas'] = nodes_room
                door_rooms[key_room]['areas_name'] = nodes_room_name

        for key, value in door_rooms.items():
            for idx, area in enumerate(value['areas']):
                ray = [area, door]
                if LineString(ray).relate_pattern(value['room'],'1FF0*F212') or \
                        (LineString(ray).intersection(value['room']).geom_type == "LineString" and\
                        abs(LineString(ray).length-LineString(ray).intersection(value['room']).length) <
                         Parameter.MIN_DISTANCE):
                    door_parent[doors.index(door)]['visible_areas'].append(value['areas_name'][idx])

        distances0 = []
        distances1 = []

        area_list0 = []
        area_list1 = []

        if len(door_parent[doors.index(door)]['visible_areas']) < 4:
            print("wait!")

        for vis_area in door_parent[doors.index(door)]['visible_areas']:
            if vis_area in nodes[door_parent[doors.index(door)]['parent_room'][0]].keys():
                distances0.append(Point(door).distance(Point(to_coordinates(vis_area))))
                area_list0.append(vis_area)
            elif vis_area in nodes[door_parent[doors.index(door)]['parent_room'][1]].keys():
                distances1.append(Point(door).distance(Point(to_coordinates(vis_area))))
                area_list1.append(vis_area)
        door_parent[doors.index(door)]['parent_area'] = [
            area_list0[distances0.index(min(distances0))],
            area_list1[distances1.index(min(distances1))]
        ]
    return door_parent

def decompose_the_floor():
    env_bb, env_coor_list, door, landmarks = data_collection()
    nodes = {}
    for key, value in env_coor_list.items():
        nodes[key] = decision_points_decomposition(value)

    landmarks = landmarks_parent_area(env_coor_list, nodes, landmarks)
    door_parent = doors_parent_area(env_coor_list, nodes, door)
    return nodes, door_parent, landmarks

def get_info():
    areas, doors, landmarks = decompose_the_floor()
    equis = {}
    for room, a_dict in areas.items():
        if len(a_dict) == 2:
            equis[list(a_dict.keys())[1]] = list(a_dict.keys())[0]

    for room, a_dict in areas.items():
        if len(a_dict) == 2:
            areas[room] = {list(a_dict.keys())[0]:{}}

    for did, info in doors.items():
        for removed in equis.keys():
            if removed in info['visible_areas']:
                info['visible_areas'].remove(removed)
            if removed in info['parent_area']:
                info['parent_area'].remove(removed)
                info['parent_area'].append(equis[removed])

    for lid, info in landmarks.items():
        for removed in equis.keys():
            if removed in info['visible_areas']:
                info['visible_areas'].remove(removed)
            if removed == info['parent_area']:
                info['parent_area'] = equis[removed]

    return areas, doors, landmarks


def cardinal_dir_calc(point_list_area, point_list_door):
    first = np.array(point_list_area)
    second = np.array([point_list_area[0], point_list_area[1] + 100])
    third = np.array(point_list_door)
    fs = second - first
    st = third - first

    angle_degree = math.degrees(
        math.atan2(st[1], st[0]) - math.atan2(fs[1], fs[0]))

    if angle_degree < 0:
        angle_degree = angle_degree + 360

    cardinal_dir = cardinal_direction(angle_degree)

    return cardinal_dir


if __name__ == "__main__":
    a,b,c = get_info()
