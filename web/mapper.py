from web.model import Model_web
from domain.model import Model_domain
import json 
class Mapper_web:
    def __init__(self):
        pass
    def to_domain(self, model_web):
        index = int(json.loads(model_web.return_index()))
        id = model_web.return_id()
        game = Model_domain(id).game(index)
        return game
    
    #При первом запуске
    def to_web(self, model_domain):
        matrix_state = json.dumps(model_domain.matrix)
        data = {
            "matrix": matrix_state,
            "id": str(model_domain.id)
        }
        game_web = Model_web.set_model(data)

        return game_web

    def create_web(self, data, id):
        game_web = Model_web.get_model(data, id)
        return game_web