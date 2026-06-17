from flask import Blueprint, request, render_template
class Route_web:
    def __init__(self, web_mapper, service):
        self.web_mapper = web_mapper
        self.service = service
        self.web_bp = Blueprint("web", __name__)
        
        # Ход игрока
        @self.web_bp.route("/move/<uuid>", methods=["POST"])
        def Move(uuid):
            data = request.get_json()
            web_model = web_mapper.create_web(data, uuid)
            domain_model = web_mapper.to_domain(web_model)
            game = service.cont_game(domain_model)
            return web_mapper(web_model)
        
        # Стартовая страница роута
        @self.web_bp.route("/", methods= ["GET"])
        def Create():
            domain_game = service.new_game()
            web_game = web_mapper.to_web(domain_game)
            test_matrix = [""] * 9
            return render_template("script.html", matrix=web_game.return_matrix(), uuid=web_game.return_id())
        
    def get_bp(self):
        return self.web_bp