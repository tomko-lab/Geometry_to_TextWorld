import json

class VisualiseEnv:
    def __init__(self, rooms, areas, landmarks, ulinks, doors):
        self.rooms = rooms
        self.areas = areas
        self.landmarks = landmarks
        self.ulinks = ulinks
        self.doors = doors

    def generate_json(self, address='game/test_real.json'):
        colors = ["#34568B", "#FF6F61", "#88B04B", "#F7CAC9", "#955251", "#B565A7", "#DD4124", "#009B77",
                  "#DFCFBE", "#55B4B0", "#EFC050"]
        room_color = {}
        for idx, room in enumerate(self.rooms):
            room_color[room.variable] = colors[idx%len(colors)]
        stations = {}
        lines = []
        for area in self.areas:
            stations[area.variable] = {'label': area.name}
        for door in self.doors:
            stations[door.variable] = {'label': door.name}

        for ulink in self.ulinks:
            line = {'shiftCoords': [0,0], 'nodes': []} # {"coords": [31, 2], "name": "StationB", "labelPos": "E"}
            line['name'] = ulink.area1.parent.name
            line['color'] = room_color[ulink.area1.parent.variable]
            line['nodes'].append({'coords': ulink.area1.coordinates, 'name': ulink.area1.variable, 'labelPos': 'N'})
            line['nodes'].append({'coords': ulink.area2.coordinates, 'name': ulink.area2.variable, 'labelPos': 'N'})
            lines.append(line)

        for door in self.doors:
            line = {'shiftCoords': [0, 0], 'nodes': []}
            line['name'] = door.area1.parent.name
            line['color'] = room_color[door.area1.parent.variable]
            line['nodes'].append({'coords': door.area1.coordinates, 'name': door.area1.variable, 'labelPos': 'N'})
            line['nodes'].append({'coords': door.coordinates, 'name': door.variable, 'labelPos': 'N'})
            lines.append(line)

            line = {'shiftCoords': [0, 0], 'nodes': []}
            line['name'] = door.area2.parent.name
            line['color'] = room_color[door.area2.parent.variable]
            line['nodes'].append({'coords': door.area2.coordinates, 'name': door.area2.variable, 'labelPos': 'N'})
            line['nodes'].append({'coords': door.coordinates, 'name': door.variable, 'labelPos': 'N'})
            lines.append(line)

        with open(address, 'w', encoding='utf-8') as fp:
            json.dump({'stations': stations, 'lines': lines}, fp)
