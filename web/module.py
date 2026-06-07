from flask import (
    Flask,
    request,
    render_template_string,
    render_template,
    request,
    session,
    jsonify,
)
class App:
    def __init__(self, blueprint):
        self.app = self.start(blueprint)
        self.app.run(host="0.0.0.0", debug=True)
    def start(self, blueprint):
        app = Flask(__name__)
        app.secret_key = "sobaka_sutulaya"
        app.register_blueprint(blueprint)
        return app