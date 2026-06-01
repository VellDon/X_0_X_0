import sqlite3
import json


def Get_data_base(user_id):
    connect = sqlite3.connect("gamebase.db")
    curs = connect.cursor()
    curs.execute("SELECT matrix FROM games WHERE user_id = ?", (user_id,))
    matrix_str = curs.fetchone()
    if matrix_str is None:
        saved_matrix = [""] * 9
    else:
        saved_matrix = json.loads(matrix_str[0])
    connect.close()
    return saved_matrix


def Save_data_base(user_id, str_matrix):
    str_matrix = json.dumps(str_matrix)
    connect = sqlite3.connect("gamebase.db")
    curs = connect.cursor()
    curs.execute(
        "REPLACE INTO games (user_id, matrix) VALUES (?, ?)", (user_id, str_matrix)
    )
    connect.commit()
    connect.close()


def Init_db():
    connection = sqlite3.connect("gamebase.db")
    curs = connection.cursor()
    curs.execute("""
    CREATE TABLE IF NOT EXISTS games (user_id TEXT PRIMARY KEY,
                 matrix TEXT)
    """)
    connection.commit()
    connection.close()
