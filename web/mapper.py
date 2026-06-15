from web.model import Model_web
from domain.model import Model_domain
import json 
class Mapper_web:
    def __init__(self):
        pass
    def to_domain(self, model_web):
        index = json.loads(model_web.return_index())
        id = model_web.return_id()
        game = Model_domain.game(index, id)
        return game
    
    def to_web(self, model_domain):
        data = {
            "index": model_domain.index,
            "matrix": model_domain.matrix,
            "id": str(model_domain.id)
        }
        game_web = Model_web.set_model(data)

    def create_web(self, data, id):
        game_web = Model_web.get_model(data, id)
        return game_web