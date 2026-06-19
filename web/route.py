from flask import Blueprint, request, render_template, jsonify
class Route_web:
    def __init__(self, web_mapper, service):
        self.web_mapper = web_mapper
        self.service = service
        self.web_bp = Blueprint("web", __name__)
        
        # Ход игрока
        @self.web_bp.route("/move/<uuid>", methods=["POST"])
        def Move(uuid):
            data = request.get_json()
            print(data)
            print(uuid)
            web_model = self.web_mapper.create_web(data, uuid)
            domain_model = self.web_mapper.to_domain(web_model)
            self.service.cont_game(domain_model)
            self.web_mapper.to_return(web_model, domain_model)
            return jsonify(web_model.request_data())
        
        # Стартовая страница роута
        @self.web_bp.route("/", methods= ["GET"])
        def Create():
            domain_game = self.service.new_game()
            web_game = self.web_mapper.to_web(domain_game)
            return render_template("script.html", matrix=web_game.return_matrix(), uuid=web_game.return_id())
        
    def get_bp(self):
        return self.web_bp