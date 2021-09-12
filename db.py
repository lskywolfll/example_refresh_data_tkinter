import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("other.db")
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS cliente(id INTEGER PRIMARY KEY, producto text, cliente text, vendedor text, precio text)")
        self.conn.commit()
    
    def insert(self, producto, cliente, vendedor, precio):
        self.cur.execute("INSERT INTO cliente (producto, cliente, vendedor, precio) VALUES (?,?,?,?)", (producto, cliente, vendedor, precio))
        self.conn.commit()
    
    def get_testing(self):
        data = list(self.cur.execute("SELECT * FROM cliente"))
        return data
    
    def __del__(self):
        self.conn.close()

if __name__ == '__main__':
    db = Database()
    # db.insert("4GB DDR4 RAM","Luis Gomez","Megacentro", "1800")
    # db.insert("Laptop", "Juan martinez", "radiochark", "18950")
    db.insert("RELOJ","Rene Sanchez", "Megacentro _ XD","1800")
    # print(db.get_testing())