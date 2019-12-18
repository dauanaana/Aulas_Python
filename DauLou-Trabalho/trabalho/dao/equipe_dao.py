from dao.base_dao import BaseDao

class EquipeDao(BaseDao):

    def listar(self):
        return super().listar('SELECT * FROM cadastroequipe')

    def inserir(self, nome_equipe, nome_linguagem):
        super().inserir(f"INSERT INTO cadastroequipe VALUES (DEFAULT, '{nome_equipe}', '{nome_linguagem}')")

    # def alterar(self):
    #     super().alterar(f"UPDATE cadastroequipe SET linguagem = ")

    def deletar(self, id):
        super().deletar(f"DELETE FROM cadastroequipe WHERE id = {id}")
