from domain.model import Model_domain
from datasource.model import Model_repos
import json
class Mapper_rep:
    def __init__(self):
        pass
    #Для начальной игры при выходе из базы
    def to_domain(self, model_rep, model_domain):
        model_domain.new_game(model_rep.str_matrix, model_rep.game_id)

        return model_domain
    
    #Используем для старта новой игры
    def to_repository(self, model_domain):
        id = model_domain.id
        matrix = [""] * 9
        data_game = Model_repos.new_game(id, matrix)
        return data_game
    
    def to_get_repository(self, domain_model):
        id = domain_model.id
        data = Model_repos.get_game(id)
        
        return data