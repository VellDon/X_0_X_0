from domain.model import Model_domain
import uuid
from game import MinMaks
class Service:
    def __init__(self, repository, mapper):
        self.repository = repository
        self.mapper_repos = mapper
    
    #Для стартовой страницы
    def new_game(self):
        id = str(uuid.uuid4())
        game = Model_domain(str(id))
        data_game = self.mapper_repos.to_repository(game)
        data_game = self.repository.Save(data_game)
        game = self.mapper_repos.to_domain(data_game, game)
        return game
    
    def cont_game(self, game):
        data_game = self.mapper_repos.to_repository(game)



        return 0