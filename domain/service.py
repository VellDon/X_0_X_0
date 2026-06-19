from domain.model import Model_domain
import uuid

class Service:
    def __init__(self, repository, mapper, minMaks):
        self.repository = repository
        self.mapper_repos = mapper
        self.minMaks = minMaks
    
    #Для стартовой страницы
    def new_game(self):
        id = str(uuid.uuid4()) #  создали айди
        print(id)
        print(type(id))
        game_domain = Model_domain(id=id, matrix=[""] * 9)
        data_game = self.mapper_repos.to_repository(game_domain)
        self.repository.Save(data_game)
        game = self.mapper_repos.to_domain(data_game)
        return game
    
    # Для хода игрока
    def cont_game(self, game_domain):
        data_game = self.mapper_repos.to_get_repository(game_domain)
        self.repository.Get(data_game)
        if data_game.err() == True:
            print("нету игры по данному айди - ERROR")
            game_domain.err_id()
        else:
            self.mapper_repos.set_to_domain(game_domain, data_game)
            
            if(self.minMaks.PlayerMove(game_domain)):
                self.mapper_repos.set_to_repos(game_domain, data_game)
                self.repository.Save(data_game)
            else:
                game_domain.err_move()
