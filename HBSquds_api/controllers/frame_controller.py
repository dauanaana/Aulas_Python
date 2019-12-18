from dao.framework_dao import FrameDao
from dao.funcoes_de_verificacao import Verificacao
from model.framework import Framework
from flask_restful import Resource
from flask import request

class FrameControllers(Resource):
    def __init__(self):
        self.dao_frame = FrameDao()
        self.dao_verifica = Verificacao()

    def get(self, id=None):
        if (id):
            return self.dao_frame.buscar_por_id(id).__dict__()
        else:
            return self.dao_frame.listar().__dict__()
    
    def post(self):
        _json = request.json
        nome = _json['nome']
        frame = Framework(nome)
        if self.dao_verifica.buscar_por_nome(nome, 'framework') == nome:
            return f'{nome} já está na tabela framework!!'
        elif self.dao_verifica.buscar_por_nome(nome, 'framework') == None:
            id_post = self.dao_frame.inserir(frame)
            return self.dao_frame.buscar_por_id(id_post).__dict__()

    def delete(self, id):
        self.dao_frame.deletar(id)
        return 'Deletado!!!'