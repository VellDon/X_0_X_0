from domain.model import Model_domain
from datasource.model import Model_repos
import json
class Mapper_rep:
    def __init__(self):
        pass
    #Для начальной игры при выходе из базы
    def to_domain(self, model_rep):
        model_domain = Model_domain(matrix=model_rep.str_matrix, id=model_rep.game_id)
        return model_domain
    
    #Используем для старта новой игры
    def to_repository(self, model_domain):
        id = model_domain.id
        matrix = model_domain.matrix
        data_game = Model_repos(id=id, matrix=matrix)
        return data_game
    
    # Используем для проверки валидации и хода
    def to_get_repository(self, domain_model):
        id = domain_model.id
        data = Model_repos(id=id)
        return data
    
    #Обновляем матрицу домен для игры
    def set_to_domain(self, domain, repos):
        matrix = repos.str_matrix
        domain.init_matrix(json.loads(matrix))

    def set_to_repos(self, domain, repos):
        matrix = domain.matrix
        repos.set_matrix(matrix)

