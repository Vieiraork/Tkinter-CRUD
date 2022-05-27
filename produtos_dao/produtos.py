from connection.connect import conn


class Produtos:
    def __init__(self) -> None:
        self.cursor = conn.cursor()

    def insert(self, product: str, price: float) -> bool:
        try:
            self.cursor.execute("""
                    INSERT INTO produtos ('produto', 'preco') VALUES (?, ?)
                    """, (product, price))
            conn.commit()
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def delete(self, identifier: int) -> bool:
        try:
            query = 'DELETE FROM produtos WHERE id = ?'
            args = (identifier, )
            self.cursor.execute(query, args)
            conn.commit()
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def select_data(self) -> list:
        try:
            result = self.cursor.execute('SELECT * FROM produtos')
            produtos = result.fetchall()
        except Exception as e:
            print(e)
        else:
            return produtos
