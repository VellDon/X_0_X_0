
class Model_domain:
    def __init__(self, id):
        self.id = id
        self.matrix = None
        self.index = None

    def game(self, index):
        self.index = index
    
    def new_game(self, matrix, id):
        self.matrix = matrix
        self.id = id
        