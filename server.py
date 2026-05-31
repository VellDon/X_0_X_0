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

app = Flask(__name__)

matrix = [["", "", ""], ["", "", ""], ["", "", ""]]


@app.route("/start")
def Hello():
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
    return render_template("script.html", matrix=matrix)


@app.route("/move", methods=["POST"])
def Move():
    data = request.get_json()
    index = int(data.get("number"))
    game = MinMaks(id=123, number=index)
    game.PlayerMove(index)

    res = game.Main()
    response = {"status": "ok", "move": res}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
