
class Model_repos:
    def __init__(self):
        self.game_id = None
        self.str_matrix = None

    def new_game(self, id, matrix):
        self.game_id = id
        self.str_matrix = matrix

    def get_game(self, id):
        self.game_id = id

