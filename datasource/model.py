
class Model_repos:
    def __init__(self, id=None, matrix=None):
        self.game_id = id
        self.str_matrix = matrix
        self.error = False
    
    #Для новой игры
    def new_game(self, id, matrix):
        self.game_id = id
        self.str_matrix = matrix

    def get_game(self, id):
        self.game_id = id

    def set_error(self):
        self.error = True

    def set_matrix(self, matrix):
        self.str_matrix = matrix
    
    def err(self):
        return self.error