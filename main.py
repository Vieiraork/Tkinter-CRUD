from connection.connect import create_database, create_file
from windows.register_window import Window
import os

if __name__ == '__main__':
    if not os.path.exists('produtos.db'):
        create_file()
    else:
        create_database()

    register_window = Window()
    register_window.run()

