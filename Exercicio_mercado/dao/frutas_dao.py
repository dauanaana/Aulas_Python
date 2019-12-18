import sys
sys.path.append('C:/Users/hbsis/Desktop/exercicio_mercado')

from dao.base_dao import BaseDao
from model.frutas_model import Frutas

class FrutasDao(BaseDao):
    
    def inserir(self, fruta:Frutas):
        comando_sql_insert = f"INSERT INTO frutas VALUES (DEFAULT, '{fruta.nome}', {fruta.preco})"
        return super().inserir(comando_sql_insert)

    def deletar(self, id):
        comando_sql_delete = f"DELETE FROM frutas WHERE id={id}"
        return super().deletar(comando_sql_delete)

    def listar(self):
        lista_frutas = []
        comando_sql_listar = f"SELECT nome, preco, id FROM frutas"
        lista_tuplas=super().listar(comando_sql_listar)
        for l in lista_tuplas:
            fruta = Frutas(l[0],l[1],l[2]).__dict__()
            lista_frutas.append(fruta)
        return lista_frutas 

    def buscar_por_id(self, id):
        comando_sql__buscar_id = f"SELECT nome, preco, id FROM frutas WHERE id = {id}"
        l = super().buscar_por_id(comando_sql__buscar_id)
        fruta = Frutas(l[0], l[1], l[2])
        return fruta.__dict__()

