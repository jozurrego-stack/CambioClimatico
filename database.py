import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).with_name("botclimatico.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS usuarios (
            user_id INTEGER PRIMARY KEY, puntos INTEGER NOT NULL DEFAULT 0,
            retos_completados INTEGER NOT NULL DEFAULT 0)""")

def agregar_puntos(user_id, cantidad=10):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT OR IGNORE INTO usuarios (user_id) VALUES (?)", (user_id,))
        conn.execute("UPDATE usuarios SET puntos=puntos+?, retos_completados=retos_completados+1 WHERE user_id=?",
                     (cantidad, user_id))
        row = conn.execute("SELECT puntos, retos_completados FROM usuarios WHERE user_id=?",
                           (user_id,)).fetchone()
    return row

def obtener_puntos(user_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("INSERT OR IGNORE INTO usuarios (user_id) VALUES (?)", (user_id,))
        row = conn.execute("SELECT puntos, retos_completados FROM usuarios WHERE user_id=?",
                           (user_id,)).fetchone()
    return row

def obtener_ranking(limite=10):
    with sqlite3.connect(DB_PATH) as conn:
        return conn.execute("SELECT user_id,puntos,retos_completados FROM usuarios ORDER BY puntos DESC LIMIT ?",
                            (limite,)).fetchall()
