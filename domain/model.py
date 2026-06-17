
class Model_domain:
    def __init__(self, id=None, matrix=None, index=None):
        self.id = id
        self.matrix = matrix
        self.index = index

    def game(self, index):
        self.index = index
    
    def new_game(self, matrix, id):
        self.matrix = matrix
        self.id = id
    
    def init_matrix(self, matrix):
        self.matrix = matrix