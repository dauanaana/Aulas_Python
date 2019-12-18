import MySQLdb

class BaseDao:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host = 'mysql.topskills.study',
            database = 'topskills14',
            user = 'topskills14',
            passwd = 'Dauana2019'
        )
        self.cursor = self.conn.cursor()

    def listar(self, sqll):
        self.cursor.execute(sqll)
        return self.cursor.fetchall()
    
    def inserir(self, sqll):
        print(sqll)
        self.cursor.execute(sqll)
        self.conn.commit()
    
    def alterar(self, sqll):
        self.cursor.execute(sqll)
        self.conn.commit()
        
    def deletar(self, sqll):
        self.cursor.execute(sqll)
        self.conn.commit()

