from dao.base_dao import BaseDao
from model.verifica import Verifica

class Verificacao(BaseDao):
    def buscar_por_nome(self, nome, nome_tabela):
        try:
            comando_sql_buscar_id = f"""SELECT 
                                    nome  
                                    FROM {nome_tabela}
                                    WHERE nome = '{nome}'"""

            l = super().buscar_por_id(comando_sql_buscar_id)
            return l[0]
        except:
            return None