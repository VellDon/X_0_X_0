from flask import (
    Flask,
    request,
    render_template_string,
    render_template,
    request,
    session,
    jsonify,
)
from game import MinMaks
import uuid
from data_base import *

app = Flask(__name__)

app.secret_key = "sobaka_sutulaya"
Init_db()
# matrix = ["", "", "", "", "", "", "", "", ""]


@app.route("/")
def Hello():
    """
    # 1. Достаем данные из URL (то, что после ?)
    name = request.args.get("name", "Stranger")
    # 2. Узнаем IP-адрес пользователя
    ip = request.remote_addr
    # 3. Узнаем, какой у пользователя браузер
    browser = request.user_agent.browser
    # 4. Узнаем метод (обычно GET)
    method = request.method
    # Выводим в консоль (черное окно), чтобы ты видел процесс «заполнения»
    print(f"--- НОВЫЙ ЗАПРОС ---")
    print(f"Кто зашел: {name}")
    print(f"IP: {ip}")
    print(f"Браузер: {browser}")
    print(f"Метод: {method}")
    """
    id = Get_user_id()
    matrix = Get_data_base(id)
    return render_template("script.html", matrix=matrix)


@app.route("/move", methods=["POST"])
def Move():
    data = request.get_json()
    index = int(data.get("number"))
    id = Get_user_id()
    user_matrix = Get_data_base(id)
    game = MinMaks(number=index)
    game.matrix = user_matrix
    if game.PlayerMove(index) == 1:
        res = game.Main()
        game.matrix[res] = "0"
        Save_data_base(id, game.matrix)
        response = {"status": "ok", "move": res, "matrix": game.matrix}
    else:
        response = {
            "status": "not",
        }

    return jsonify(response)


def Get_user_id():
    user_id = session.get("user_id")
    if not user_id:
        user_id = str(uuid.uuid4())
        session["user_id"] = user_id
    return user_id


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
