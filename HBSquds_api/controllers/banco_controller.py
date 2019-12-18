from dao.banco_dao import BancoDao
from dao.funcoes_de_verificacao import Verificacao
from model.bd import BD
from flask_restful import Resource
from flask import request

class BancoControllers(Resource):
    def __init__(self):
        self.dao_bd = BancoDao()
        self.dao_verifica = Verificacao()

    def get(self, id=None):
        if id:
            return self.dao_bd.buscar_por_id(id).__dict__()
        else:
            return self.dao_bd.listar().__dict__()
    
    def post(self):
        _json = request.json
        nome = _json['nome']
        banco = BD(nome)
        if self.dao_verifica.buscar_por_nome(nome, 'banco') == nome:
            return f'{nome} já está na tabela banco!!'
        elif self.dao_verifica.buscar_por_nome(nome, 'banco') == None:
            id_post = self.dao_bd.inserir(banco)
            return self.dao_bd.buscar_por_id(id_post).__dict__()

    def delete(self, id):
        self.dao_bd.deletar(id)
        return 'Deletado!!!'