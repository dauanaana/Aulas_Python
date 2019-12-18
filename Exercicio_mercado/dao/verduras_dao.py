import sys
sys.path.append('C:/Users/hbsis/Desktop/exercicio_mercado')

from dao.base_dao import BaseDao
from model.verduras_model import Verduras

class VerdurasDao(BaseDao):

    def inserir(self, verdura:Verduras):
        comando_sql_insert = f"INSERT INTO verduras VALUES(DEFAULT, '{verdura.nome}', {verdura.preco})"
        return super().inserir(comando_sql_insert)

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM verduras WHERE id={id}"
        return super().deletar(comando_sql_delete)
    
    def listar(self):
        lista_verdura = []
        comando_sql_listar = f"SELECT nome, preco, id FROM verduras"
        lista_tuplas=super().listar(comando_sql_listar)
        for l in lista_tuplas:
            verduras = Verduras(l[0], l[1], l[2]).__dict__()
            lista_verdura.append(verduras)
        return lista_verdura
    
    def buscar_por_id(self, id):
        comando_sql__buscar_id = f"SELECT nome,preco, id FROM verduras WHERE id={id}"
        l = super().buscar_por_id(comando_sql__buscar_id)
        verduras = Verduras(l[0], l[1], l[2])
        return verduras.__dict__()
