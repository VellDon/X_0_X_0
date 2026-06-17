from domain.model import Model_domain
import uuid
from game import MinMaks
class Service:
    def __init__(self, repository, mapper):
        self.repository = repository
        self.mapper_repos = mapper
    
    #Для стартовой страницы
    def new_game(self):
        id = str(uuid.uuid4()) #  создали айди
        game_domain = Model_domain(id=id, matrix=[""] * 9)
        data_game = self.mapper_repos.to_repository(game_domain)
        self.repository.Save(data_game)
        game = self.mapper_repos.to_domain(data_game)
        return game
    
    # Для хода игрока
    def cont_game(self, game_domain):
        data_game = self.mapper_repos.to_get_repository(game_domain)
        self.repository.Get(data_game)
        self.mapper_repos.set_to_domain(game_domain, data_game)







        return 0