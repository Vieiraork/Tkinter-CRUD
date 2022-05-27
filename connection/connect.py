import sqlite3

conn = sqlite3.connect('produtos.db')
# SQLAlchemy


def create_database() -> None:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS produtos (\
	    id INTEGER PRIMARY KEY AUTOINCREMENT,\
	    produto TEXT NOT NULL,\
	    preco REAL NOT NULL\
    );")
    cursor.close()


def create_file() -> None:
    arquivo = open('produtos.db', 'w')
    arquivo.close()
