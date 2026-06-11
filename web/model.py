
class Model_web:
    def __init__(self, data):
      self.set_model(data)

    def set_model(self, data):
        self.matrix = data["matrix"]
        self.id = data["id"]
        self.numer_move = data["index"]
    def get_model():
        return 0