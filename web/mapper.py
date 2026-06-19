from web.model import Model_web
from domain.model import Model_domain
import json 
class Mapper_web:
    def __init__(self):
        pass

    # Для обработки хода игрока
    def to_domain(self, model_web):
        index = int(model_web.return_index())
        id = model_web.return_id()
        game = Model_domain(id=id, index=index)
        return game
    
    #При первом запуске
    def to_web(self, model_domain):
        matrix_state = json.dumps(model_domain.matrix)
        data = {
            "matrix": matrix_state,
            "id": str(model_domain.id)
        }
        game_web = Model_web()
        game_web.set_model(data)
        return game_web
    
    # Для обработки хода игрока
    def create_web(self, data, id):
        index = data["number"]
        game_web = Model_web(index=index, id=id)
        return game_web
    
    def to_return(self, web, domain):
        data = {}
        if domain.err_no_id == "yes" or domain.err_no_move == "yes":
          data["status"] = "not"
        else:
            data["status"] = "ok"
            data["move"] = domain.move
            data["win"] = domain.win
        
        web.init_data(data)
