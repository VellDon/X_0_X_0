
class Model_web:
    def __init__(self, index=None, matrix=None, id=None):
        self.index = index
        self.matrix = matrix
        self.id = id
        self.data = None

    def set_model(self, data):
        self.matrix = data["matrix"]
        self.id = data["id"]

    def return_matrix(self):
        return self.matrix
    
    def return_id(self):
        return self.id
    
    def return_index(self):
        return self.index
    
    def get_model(self, data, id):
        self.index = data["index"]
        self.id = id

    def init_data(self, data):
        self.data = data
        
    def request_data(self):
        print(self.data)
        return self.data
