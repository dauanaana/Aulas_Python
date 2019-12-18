import MySQLdb
from pessoa import Pessoa

class Funcionario:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host = 'mysql.topskills.study',
            database = 'topskills14',
            user = 'topskills14',
            passwd = 'Dauana2019'
        )
        self.cursor = self.conn.cursor()

    #***cadastrar funcionario
    def cadastrar(self, nome, sobrenome, identidade):
            pessoa.id = self.gerar_id
            self.cursor.execute(f'insert into cadastrofunc (nome, sobrenome, identidade) values ("{nome}", "{sobrenome}", "{identidade}")')
            self.conn.commit()
            print('Dados inseridos com sucesso.')


    #***listar funcionario cadastrado
        def listar(self):
            self.cursor.execute('select * from cadastrofunc')
            lista = self.cursor.fetchall()
            return lista


    

        def buscar_por_id(self, id:int):
            self.cursor.execute(f'select * from cadastrofunc where id = {id}')
            item = self.cursor.fetchone()    
            return item

        def alterar(self, nome, sobrenome, identidade, id:int):
            self.cursor.execute(f'update cadastrofunc set nome = "{nome}", "{sobrenome}", "{identidade}" where id = {id}')
            self.conn.commit()

        def deletar(self, id:int):
            self.cursor.execute(f'delete from cadastrofunc where id = {id}')
            self.conn.commit()
