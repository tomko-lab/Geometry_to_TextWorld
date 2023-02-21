class Parameter:
    ENV_SIMPLE = False
    DATASET_DIRECTORY = "dataset/"
    DOORS = 'doors.geojson'
    ENV = 'env.geojson'
    LANDMARKS = 'landmarks.geojson'
    GAME_ADDRESS = 'game/test_real.z8'
    MIN_DISTANCE = 1
    PLAYER = 'a1r1'

    @staticmethod
    def setScenario(isSimple=ENV_SIMPLE):
        if isSimple:
            Parameter.DATASET_DIRECTORY = "dataset/simple/"
            Parameter.GAME_ADDRESS = 'game/simple_test.z8'
            Parameter.MIN_DISTANCE = 5
            Parameter.PLAYER = 'a0r0'