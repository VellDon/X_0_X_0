import sqlite3
import json
from datasource.model import Model_repos
class Repository:
    def __init__(self):
        self.Init_db()

    def Init_db():
        connection = sqlite3.connect("gamebase.db")
        curs = connection.cursor()
        curs.execute("""
        CREATE TABLE IF NOT EXISTS games (user_id TEXT PRIMARY KEY,
                 matrix TEXT)
        """)
        connection.commit()
        connection.close()

    def Get(model):
        connect = sqlite3.connect("gamebase.db")
        curs = connect.cursor()
        curs.execute("SELECT matrix FROM games WHERE user_id = ?", (model.game_id,))
        matrix_str = curs.fetchone()
        if matrix_str is None:
            saved_matrix = [""] * 9
        else:
            saved_matrix = json.loads(matrix_str[0])
        connect.close()
        return saved_matrix


    def Save_data_base(model):
        str_matrix = json.dumps(str_matrix)
        connect = sqlite3.connect("gamebase.db")
        curs = connect.cursor()
        curs.execute(
            "REPLACE INTO games (user_id, matrix) VALUES (?, ?)", (model.game_id, model.str_matrix)
        )
        connect.commit()
        connect.close()