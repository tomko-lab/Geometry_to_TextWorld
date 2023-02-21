import direction
from concepts import Player, IndoorArea, IndoorRoom, ULink, Door, Landmark
import textworld.generator.inform7.world2inform7 as compiler
import textworld
import logging
import templates
import vertex_decompose
from visualization import VisualiseEnv
from parameters import Parameter

logging.basicConfig(level=logging.DEBUG)

class I7Generator:
    def __init__(self, areas, doors, landmarks, win_area, max_interaction):
        self.is_there_a_quest = True
        self.areas = areas
        self.doors = doors
        self.landmarks = landmarks
        self.win_area = win_area
        self.max_interaction = max_interaction


    def generate_game(self, address):
        # create player
        player = Player()
        player.set_orientation(4)

        room_list = []
        area_dictionary = {}
        for rid, ainfo in self.areas.items():
            room = IndoorRoom(variable='r{}'.format(rid), name='Room {}'.format(rid), description='Room {}'.format(rid))
            local_areas = []
            for idx, aid in enumerate(list(ainfo.keys())):
                area = IndoorArea(variable='a{0}r{1}'.format(idx, rid),
                                  name='Area {0} in Room {1}'.format(idx, rid),
                                  description='An area ({0}) in [parent]'.format(idx), parent=room,
                                  coordinates=vertex_decompose.to_coordinates(aid))
                area_dictionary['a{0}r{1}'.format(idx, rid)] = area
                local_areas.append(area)
            room_list.append(room)

        ulinks = []
        for rid, ainfo in self.areas.items():
            for idx, aid in enumerate(list(ainfo.keys())):
                id_list = list(ainfo.keys())
                area1 = area_dictionary['a{0}r{1}'.format(idx, rid)]
                connections = ainfo[aid]
                for connection in connections.keys():
                    idx2 = id_list.index(connection)
                    area2 = area_dictionary['a{0}r{1}'.format(idx2, rid)]
                    ulink = ULink(area1, area2, direction.abbrv_directions[connections[connection]])
                    ulinks.append(ulink)

        door_list = []
        for did, info in self.doors.items():
            relation = vertex_decompose.cardinal_dir_calc(
                vertex_decompose.to_coordinates(info['parent_area'][0]), info['geometry'])
            relation2 = vertex_decompose.cardinal_dir_calc(
                vertex_decompose.to_coordinates(info['parent_area'][1]), info['geometry'])
            d_area_keys = []
            for aid in info['parent_area']:
                for rid in info['parent_room']:
                    all_area_keys_in_a_room = list(self.areas[rid].keys())
                    if aid in all_area_keys_in_a_room:
                        d_a_key = 'a{0}r{1}'.format(all_area_keys_in_a_room.index(aid), rid)
                        d_area_keys.append(d_a_key)
                        break

            door = Door(variable='d{}'.format(did),
                        name='Door Room {0} to Room {1}'.format(info['parent_room'][0], info['parent_room'][1]),
                        description='Door Room {0} to Room {1}'.format(info['parent_room'][0], info['parent_room'][1]),
                        area1=area_dictionary[d_area_keys[0]], area2=area_dictionary[d_area_keys[1]],
                        relation=direction.abbrv_directions[relation], coordinates=info['geometry'])
            door_list.append(door)


        landmark_list = []
        for lid, info in self.landmarks.items():
            l_area = None
            info['parent_area'] = info['parent_area'].replace('.0, ', ', ').replace('.0]', ']')
            for rid, ainfo in self.areas.items():
                if info['parent_area'] in ainfo.keys():
                    aidx = list(ainfo.keys()).index(info['parent_area'])
                    l_a_key = 'a{0}r{1}'.format(aidx, rid)
                    l_area = area_dictionary[l_a_key]
                    break
            if l_area is None:
                print('yaaaaa babaaaaam!!!!')
            landmark = Landmark(variable='landmark{}'.format(lid),
                                name='Landmark {}'.format(lid), description=info['description'],
                                area=l_area)
            l_area.visible_landmarks.append(landmark)
            landmark_list.append(landmark)

        snippets = []
        # define concepts
        snippets.append(IndoorRoom.define_concept())
        snippets.append(IndoorArea.define_concept())
        snippets.append(Player.define_concept())
        snippets.append(Door.define_concept())
        snippets.append(Landmark.define_concept())

        # define instances
        snippets.extend([instance.define_instance() for instance in room_list])
        snippets.extend([instance.define_instance() for instance in area_dictionary.values()])
        snippets.extend([instance.define_instance() for instance in ulinks])
        snippets.extend([instance.define_instance() for instance in door_list])
        snippets.extend([instance.define_instance() for instance in landmark_list])
        snippets.extend([instance.define_visible_landmarks() for instance in area_dictionary.values()])

        snippets.append(templates.FIXED_VIABLE_DIRECTIONS)
        snippets.append(templates.FIXED_ACTIONS)
        snippets.append(templates.FIXED_DIRECTION_DEFINITION)
        snippets.append(templates.FIXED_ALTERNATIVE_NAMES)

        snippets.append(player.set_player_in_area(area_dictionary[Parameter.PLAYER]))
        snippets.append(player.define_instance())
        snippets.append(templates.QUESTI_DEFINITION.format(max_interaction=self.max_interaction,
                                                           win_area=self.win_area))

        logging.info('\n'.join(snippets))
        compiler.compile_inform7_game('\n'.join(snippets), address)
        logging.info('game is generated')

        # visualise = VisualiseEnv(room_list, list(area_dictionary.values()), landmark_list, ulinks, door_list)
        # visualise.generate_json()

    @staticmethod
    def test():
        # create player
        player = Player()
        player.set_orientation(0)

        # create concepts
        roomA = IndoorRoom(variable='iA', name='Room A', description='Room A')
        roomB = IndoorRoom(variable='iB', name='Room B', description='Room B')
        roomC = IndoorRoom(variable='iC', name='Room C', description='Room C')
        roomD = IndoorRoom(variable='iD', name='Room D', description='Room D')
        roomE = IndoorRoom(variable='iE', name='Room E', description='Room E')

        area1 = IndoorArea(variable='area1', name='A1', description= 'An area in [parent]', parent=roomA)
        area2 = IndoorArea(variable='area2', name='A2', description='An area in [parent]', parent=roomA)
        area3 = IndoorArea(variable='area3', name='A3', description='An area in [parent]', parent=roomB)
        area4 = IndoorArea(variable='area4', name='A4', description='An area in [parent]', parent=roomB)
        area5 = IndoorArea(variable='area5', name='A5', description='An area in [parent]', parent=roomC)
        area6 = IndoorArea(variable='area6', name='A6', description='An area in [parent]', parent=roomD)
        area7 = IndoorArea(variable='area7', name='A7', description='An area in [parent]', parent=roomE)

        ulink1 = ULink(area1, area2, 'north')
        ulink2 = ULink(area3, area4, 'north')

        door1 = Door(variable='doorAB', name='Door A to B', description='Door A to B', area1=area2, area2=area3,
                     relation='north')
        door2 = Door(variable='doorBC', name='Door B to C', description='Door B to C', area1=area4, area2=area5,
                     relation='west')
        door3 = Door(variable='doorAD', name='Door A to D', description='Door A to D', area1=area1, area2=area6,
                     relation='east')
        door4 = Door(variable='doorAE', name='Door A to E', description='Door A to E', area1=area1, area2=area7,
                     relation='northeast')

        landmark1 = Landmark(variable='l1', name='dummy statue', description='A very dummy statue '
                                                                             'in the middle of nowhere!', area=area1)
        area2.visible_landmarks.append(landmark1)

        snippets = []
        # define concepts
        snippets.append(IndoorRoom.define_concept())
        snippets.append(IndoorArea.define_concept())
        snippets.append(Player.define_concept())
        snippets.append(Door.define_concept())
        snippets.append(Landmark.define_concept())

        #define instances
        snippets.extend([instance.define_instance() for instance in [roomA, roomB, roomC, roomD, roomE,
                                                                     area1, area2, area3, area4, area5, area6, area7,
                                                                     door4, door1, door2, door3, ulink1, ulink2,
                                                                     landmark1]])
        snippets.extend([area.define_visible_landmarks() for area in [area1, area2, area3, area4, area5,
                                                                      area6, area7]])

        snippets.append(templates.FIXED_VIABLE_DIRECTIONS)
        snippets.append(templates.FIXED_ACTIONS)
        snippets.append(templates.FIXED_DIRECTION_DEFINITION)
        snippets.append(templates.FIXED_ALTERNATIVE_NAMES)

        snippets.append(player.set_player_in_area(area1))
        snippets.append(templates.QUESTI_DEFINITION.format(max_interaction=6, win_area='a0r0'))

        try:
            print('\n'.join(snippets))
            compiler.compile_inform7_game('\n'.join(snippets), 'game/test.z8')
        except:
            print('wait!')
        return 'done'


if __name__ == '__main__':
    Parameter.setScenario(isSimple=True)
    areas, doors, landmarks = vertex_decompose.get_info()
    generators = I7Generator(areas, doors, landmarks, 'a0r0', 15)
    generators.generate_game(Parameter.GAME_ADDRESS)
    # textworld.play(Parameter.GAME_ADDRESS)
