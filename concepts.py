import logging
import direction
import templates

logging.basicConfig(level=logging.INFO)

class I7Concept:
    def __init__(self):
        self.kind = ''

    @staticmethod
    def define_concept():
        return ""

    def define_instance(self):
        return ""

class Player (I7Concept):
    kind = 'player'

    def __init__(self):
        self.variable = 'player'
        self.name = 'player'
        self.orietnation = 0

    def get_orientation(self):
        return self.orietnation

    def set_orientation(self, value):
        self.orietnation = value

    def __str__(self):
        return "Player class, name {}".format(self.name)

    def set_player_in_area(self, area):
        return templates.SET_IN_AREA.format(thing=self.variable, area=area.variable)

    def define_instance(self):
        return templates.DEFINE_INSTANCE_PROPERTY.format(property='orientation', instance=self.name,
                                                         value=self.orietnation)

    @staticmethod
    def define_concept():
        return templates.DEFINE_CONCEPT_PROPERTY.format(concept='player', kind='number', var='orientation')


class IndoorRoom(I7Concept):
    kind = 'indoor_room'

    def __init__(self, variable, name, description):
        self.variable = variable
        self.name = name
        self.description = description
        self.areas = []

    def add_area_to_list(self, area):
        self.areas.append(area)

    def __str__(self):
        return "An indoor room called {0} with {1} areas".format(self.name, len(self.areas))

    @staticmethod
    def define_concept():
        definition = templates.DEFINE_CONCEPT.format(concept=IndoorRoom.kind, kind='room')
        definition += templates.DEFINE_CONCEPT_PROPERTY.format(concept=IndoorRoom.kind, kind='text', var='description')
        definition += templates.DEFINE_CONCEPT_PROPERTY.format(concept=IndoorRoom.kind, kind='text', var='printed name')
        return definition

    def define_instance(self):
        definition = templates.DEFINE_INSTANCE.format(instance=self.variable, concept=IndoorRoom.kind,
                                                      description=self.description)
        return definition


class IndoorArea(I7Concept):
    kind = 'area'

    def __init__(self, variable, name, description, parent, visilbe_landmarks=[], coordinates=None):
        self.variable = variable
        self.name = name
        self.description = description
        self.parent = parent
        self.visible_landmarks = []
        self.coordinates = coordinates

    def get_parent(self):
        return self.parent

    def __str__(self):
        return "An indoor area called {0}, inside an indoor room called {1}".format(self.name, self.parent.name)

    @staticmethod
    def define_concept():
        definition = templates.DEFINE_CONCEPT.format(concept=IndoorArea.kind, kind='room')
        definition += templates.DEFINE_CONCEPT_PROPERTY.format(concept=IndoorArea.kind, kind='text', var='description')
        definition += templates.DEFINE_CONCEPT_PROPERTY.format(concept=IndoorArea.kind, kind='text', var='printed name')
        definition += templates.DEFINE_CONCEPT_PROPERTY.format(concept=IndoorArea.kind, kind=IndoorRoom.kind,
                                                               var='parent')
        definition += templates.DEFINE_CONCEPT_ABLE.format(concept=IndoorArea.kind, ability='enterable')
        definition += templates.DEFINE_CONCEPT_ALWAYS_ABLE.format(concept=IndoorArea.kind, ability='enterable')
        return definition

    def define_instance(self):
        definition = templates.DEFINE_INSTANCE.format(instance=self.variable, concept=IndoorArea.kind,
                                                      description=self.description)

        definition += templates.DEFINE_INSTANCE_PROPERTY.format(instance=self.variable, property='printed name',
                                                                value='"{}"'.format(self.parent.name))
        definition += templates.UNDERSTAND_AS.format(text=self.name, variable=self.variable)
        definition += templates.DEFINE_INSTANCE_PROPERTY.format(instance=self.variable, property='parent',
                                                                value=self.parent.variable)
        return definition

    def define_visible_landmarks(self):
        if len(self.visible_landmarks) == 0:
            return ""
        return templates.DEFINE_INSTANCE_PROPERTY.format(instance=self.variable, property='visible_objects',
                                                         value='{'+'{0}'.format(', '.join([
                                                             l.variable for l in self.visible_landmarks]))+'}')

class ULink(I7Concept):
    def __init__(self, area1, area2, relation):
        self.area1 = area1
        self.area2 = area2
        self.relation = relation

    @staticmethod
    def define_concept():
        return ""

    def define_instance(self):
        return templates.DEFINE_DIRECTION_AREAS.format(area1=self.area1.variable,
                                                       area2=self.area2.variable, relation=self.relation,
                                                       rev_relation=direction.re_directions_dict[self.relation])

class Door(I7Concept):
    kind = 'door'

    def __init__(self, variable, name, description, area1, relation, area2, relation2=None, coordinates=None):
        self.variable = variable
        self.name = name
        self.description = description
        self.area1 = area1
        self.relation1 = relation
        if relation2 is None:
            self.relation2 = direction.re_directions_dict[relation]
        else:
            self.relation2 = relation2
        self.area2 = area2
        self.coordinates = coordinates

    def __str__(self):
        return "A door that is {0} of {1} and {2} of {3}".format(self.relation1, self.area1, self.relation2, self.area2)

    @staticmethod
    def define_concept():
        return ""

    def define_instance(self):
        definition = templates.DEFINE_INSTANCE.format(instance=self.variable, concept=Door.kind,
                                                      description=self.description)
        definition += templates.DEFINE_DIRECTION_AREAS_DOORS.format(door=self.variable,
                                                                    relation=self.relation1,
                                                                    rev_relation=self.relation2,
                                                                    area1=self.area1.variable,
                                                                    area2=self.area2.variable)
        return definition


class Landmark(I7Concept):
    kind = 'landmark'

    def __init__(self, variable, name, description, area):
        self.variable = variable
        self.name = name
        self.description = description
        self.area = area

    @staticmethod
    def define_concept():
        definition = templates.DEFINE_CONCEPT.format(concept=Landmark.kind, kind='thing')
        definition += templates.DEFINE_CONCEPT_PROPERTY.format(concept=Landmark.kind, kind='text', var='description')
        definition += templates.DEFINE_CONCEPT_PROPERTY.format(concept=Landmark.kind, kind='text', var='printed name')
        definition += templates.DEFINE_CONCEPT_ABLE.format(concept=Landmark.kind, ability='examined')
        definition += templates.DEFINE_CONCEPT_PROPERTY.format(concept=IndoorArea.kind, kind='list of landmark',
                                                               var='visible_objects')
        return definition

    def define_instance(self):
        definition = templates.DEFINE_INSTANCE.format(instance=self.variable, concept=Landmark.kind,
                                                      description=self.description)
        definition += templates.DEFINE_INSTANCE_PROPERTY.format(instance=self.variable, property='printed name',
                                                                value='"{}"'.format(self.name))
        definition += templates.UNDERSTAND_AS.format(text=self.name, variable=self.variable)
        definition += self.set_in_area()
        return definition

    def set_in_area(self):
        return templates.SET_IN_AREA.format(thing=self.variable, area=self.area.variable)

    def __str__(self):
        return "{0} is a landmark called {1}, and described as {2}".format(self.variable, self.name, self.description)


if __name__ == "__main__":
    print('testing...')