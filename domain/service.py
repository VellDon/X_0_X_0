from domain.model import Model_domain
import uuid
class Service:
    def __init__(self, repository, mapper):
        self.repository = repository
        self.mapper_repos = None
    def new_game():
        id = str(uuid.uuid4())
        game = Model_domain(id)
        return game
    
    def cont_game(game):
        return 0