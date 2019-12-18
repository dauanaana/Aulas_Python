from model.bd import BD
from model.framework import Framework
from model.linguagem import Linguagem

class HB:
    def __init__(self, nome, tipo_db:BD, tipo_framework:Framework, tipo_linguagem:Linguagem, id=None):
        self.__nome = nome
        self.__bd = tipo_db
        self.__framework = tipo_framework
        self.__linguagem = tipo_linguagem
        self.__id = id

    @property
    def nome(self):
        return self.__nome

    @property
    def bd(self):
        return self.__bd

    @property
    def framework(self):
        return self.__framework

    @property
    def linguagem(self):
        return self.__linguagem

    @property
    def id(self):
        return self.__id

        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @bd.setter
    def bd(self, bd):
        self.__bd = bd
    
        
    @framework.setter
    def framework(self, framework):
        self.__framework = framework

    @linguagem.setter
    def linguagem(self, linguagem):
        self.__linguagem = linguagem

    @id.setter
    def id(self, id):
        self.__id = id

    def __dict__(self):
        return {
            "nome": self.nome,
            "fk_banco": self.bd,
            "fk_framework": self.framework,
            "fk_linguagem": self.linguagem,
            "id": self.id
        }