
class Model_web:
    def __init__(self):
        self.index = None
        self.matrix = None
        self.id = None

    def set_model(self, data):
        self.index = data["index"]
        self.matrix = data["matrix"]
        self.id = data["id"]
        return 0
    def get_model():
        return 0