from domain.model import Model_domain
import uuid
from game import MinMaks
class Service:
    def __init__(self, repository, mapper):
        self.repository = repository
        self.mapper_repos = mapper

    def new_game(self):
        id = str(uuid.uuid4())
        game = Model_domain(id)
        data_game = self.mapper_repos.to_repository(game)
        self.repository.Save(data_game)
        return game
    
    def cont_game(self, game):

        return 0