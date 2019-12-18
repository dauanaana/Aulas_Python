from dao.base_dao import BaseDao
from model.funcionario import Funcionario

class FuncionarioDao(BaseDao):

    def listar(self):
        return super().listar('SELECT * FROM cadastrofunc')

    def inserir(self, nome, sobrenome, identidade, cargo, salario):
        super().inserir(f'INSERT INTO cadastrofunc VALUES (DEFAULT, "{nome}", "{sobrenome}", "{identidade}", "{cargo}", "{salario}")')

    def alterar(self, nome, sobrenome, identidade, cargo, salario):
        super().alterar(f'UPDATE * cadastrofunc SET {nome} , {sobrenome} , {identidade} , {cargo} , {salario}')

    def deletar(self, id):
        super().deletar(f'DELETE FROM cadastrofunc where id = {id}')



   