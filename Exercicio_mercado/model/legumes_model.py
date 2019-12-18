class Legumes():
    def __init__(self, nome, preco, id=None):
        self.__nome = nome
        self.__preco = preco
        self.__id = id
        
    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco
    
    @property
    def id(self):
        return self.__id

    @nome.setter
    def nome(self, nome):
        self .__nome = nome

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @id.setter
    def id(self, id):
        self.__id = id
    
    def __dict__(self):
        return {
            "nome":self.nome,
            "preco":self.preco,
            "id":self.id
        }