import sys
sys.path.append('C:/Users/hbsis/Desktop/exercicio_mercado')

from dao.base_dao import BaseDao
from model.legumes_model import Legumes

class LegumesDao(BaseDao):
    
    def inserir(self, legume:Legumes):
        comando_sql_insert = f"INSERT INTO legumes VALUES (DEFAULT, '{legume.nome}', {legume.preco})"
        return super().inserir(comando_sql_insert)

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM legumes WHERW id={id}"
        return super().deletar(comando_sql_delete)

    def listar(self):
        lista_legumes = []
        comando_sql_listar = "SELECT nome, preco, id FROM legumes"
        lista_tuplas = super().listar(comando_sql_listar)
        for l in lista_tuplas:
            legumes = Legumes(l[0], l[1], l[2]).__dict__()
            lista_legumes.append(legumes)
        return lista_legumes
    
    def buscar_por_id(self, id):
        comando_sql_buscar_id = f"SELECT nome, preco FROM legumes WHERE id={id}"
        l = super().buscar_por_id(comando_sql_buscar_id)
        legumes = Legumes(l[0], l[1], l[2])
        return legumes.__dict__()