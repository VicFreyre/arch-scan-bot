import sqlite3
from flask import g
from config import DB_PATH

def get_db():
    db = getattr(g, "_db", None)
    if db is None:
        need_init = not DB_PATH.exists()
        db = sqlite3.connect(str(DB_PATH))
        db.row_factory = sqlite3.Row
        g._db = db
        if need_init:
            init_db(db)
    return db

def init_db(db_conn):
    cur = db_conn.cursor()
    cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        bio TEXT
    )
    """)
    cur.executemany(
        "INSERT INTO users (username, email, bio) VALUES (?, ?, ?)",
        [
            ("alice", "alice@example.local", "Analista de segurança"),
            ("bob", "bob@example.local", "Dev backend"),
            ("carol", "carol@example.local", "Estudante")
        ]
    )
    db_conn.commit()

def init_app(app):
    @app.teardown_appcontext
    def close_db(exc):
        db = getattr(g, "_db", None)
        if db is not None:
            db.close()
