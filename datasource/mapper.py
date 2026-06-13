from domain.model import Model_domain
from datasource.model import Model_repos
class Mapper_rep:
    def __init__(self):
        pass

    def to_domain(self, model_rep):
        return 0
    
    def to_repository(self, model_domain):
        id = model_domain.id
        matrix = model_domain.matrix
        data_game = Model_repos.new_game(id, matrix)
        return data_game
    
    def to_get_repository(self, domain_model):
        id = domain_model.id
        data = Model_repos.get_game(id)
        
        return data