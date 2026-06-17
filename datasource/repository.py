import sqlite3
import json
from datasource.model import Model_repos
class Repository:
    def __init__(self):
        self.Init_db()

    def Init_db(self):
        connection = sqlite3.connect("gamebase.db")
        curs = connection.cursor()
        curs.execute("""
        CREATE TABLE IF NOT EXISTS games (user_id TEXT PRIMARY KEY,
                 matrix TEXT)
        """)
        connection.commit()
        connection.close()

    def Get(self, model):
        connect = sqlite3.connect("gamebase.db")
        curs = connect.cursor()
        curs.execute("SELECT matrix FROM games WHERE user_id = ?", (model.game_id,))
        matrix_str = curs.fetchone()
        if matrix_str is None:
            model.error()
        else:
            saved_matrix = json.loads(matrix_str[0])
            model.set_matrix(saved_matrix)
        connect.close()

    # Сохраняем в базу новый ключ и игру
    def Save(self, model):
        user_id = json.dumps(model.game_id)
        matrix = json.dumps(model.str_matrix)
        connect = sqlite3.connect("gamebase.db")
        curs = connect.cursor()
        curs.execute(
            "REPLACE INTO games (user_id, matrix) VALUES (?, ?)", (user_id, matrix)
        )
        connect.commit()
        connect.close()