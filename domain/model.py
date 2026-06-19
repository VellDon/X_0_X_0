
class Model_domain:
    def __init__(self, id=None, matrix=None, index=None):
        self.id = id
        self.matrix = matrix
        self.index = index
        self.err_no_id = None
        self.err_no_move = None
        self.move = None
        self.win = None

    def game(self, index):
        self.index = index
    
    def new_game(self, matrix, id):
        self.matrix = matrix
        self.id = id
    
    def init_matrix(self, matrix):
        self.matrix = matrix

    def err_id(self):
        self.err_no_id = "yes"

    def err_move(self):
        self.err_no_move = "yes"
    
    def bot(self, index):
        self.move = index
        
    def Win(self, win):
        self.win = win