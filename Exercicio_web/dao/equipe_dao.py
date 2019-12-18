from dao.base_dao import BaseDao
from model.equipe import Equipe

class EquipeDao(BaseDao):

    def listar(self):
        return super().listar('SELECT * FROM cadastroequipe')

    def inserir(self, nome_equipe):
        super().inserir(f"INSERT INTO cadastroequipe VALUES(DEFAULT,{nome_equipe}")

    def alterar(self):
        super().alterar(f"UPDATE cadastroequipe SET linguagem = ")

    def deletar(self, id):
        super().deletar(f"DELETE FROM cadastroequipe WHERE id = {id}")
