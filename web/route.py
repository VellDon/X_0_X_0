from flask import Blueprint
class Route_web:
    def __init__(self, web_mapper):
        self.web_mapper = web_mapper
        self.web_bp = Blueprint("web", __name__)

        @self.web_bp.route("/")
        def Hello():
    
            return 0

        @self.web_bp.route("/move", methods=["POST"])
        def Move():
            return 0

            
        @self.web_bp.route("/create", methods= ["GET"])
        def Create():
            return 0
        
    def get_bp(self):
        return self.web_bp