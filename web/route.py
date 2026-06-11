from flask import Blueprint, request
class Route_web:
    def __init__(self, web_mapper, service):
        self.web_mapper = web_mapper
        self.service = service
        self.web_bp = Blueprint("web", __name__)

        @self.web_bp.route("/move", methods=["POST"])
        def Move():
            data = request.get_json()
            web_model = web_model(data)
            return web_mapper(web_model)

        @self.web_bp.route("/", methods= ["GET"])
        def Create():
            domain_game = service.
            return 0
        
    def get_bp(self):
        return self.web_bp