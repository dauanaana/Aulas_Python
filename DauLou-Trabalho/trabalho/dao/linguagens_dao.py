from dao.base_dao import BaseDao
from model.linguagens import Linguagem

class LinguagensDao(BaseDao):

    def listar(self):
        return super().listar('SELECT * FROM cadastroling')

    def inserir(self, tipolinguagem):
        super().inserir(f"INSERT INTO cadastroling  VALUES (DEFAULT,'{tipolinguagem}')")

    def alterar(self, tipolinguagem):
        super().alterar(f" UPDATE cadastroling SET nome = ' {tipolinguagem}' WHERE id = {tipolinguagem} " )
       
    def deletar(self, id):
        super().deletar(f" DELETE FROM cadastroling WHERE id = {id}")
