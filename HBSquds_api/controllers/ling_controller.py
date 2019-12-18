from dao.linguagem_dao import LingDao
from dao.funcoes_de_verificacao import Verificacao
from model.linguagem import Linguagem
from flask_restful import Resource
from flask import request

class LingControllers(Resource):
    def __init__(self):
        self.dao_ling = LingDao()
        self.dao_verifica = Verificacao()

    def get(self, id=None):
        if (id):
            return self.dao_ling.buscar_por_id(id).__dict__()
        else:
            return self.dao_ling.listar()
    
    def post(self):
        _json = request.json
        nome = _json['nome']
        lingua = Linguagem(nome)
        if self.dao_verifica.buscar_por_nome(nome, 'linguagens') == nome:
            return f'{nome} já está na tabela linguagens!!'
        elif self.dao_verifica.buscar_por_nome(nome, 'linguagens') == None:
            id_post = self.dao_ling.inserir(lingua)
            return self.dao_ling.buscar_por_id(id_post).__dict__()

    def delete(self, id):
        self.dao_ling.deletar(id)
        return 'Deletado!!!'