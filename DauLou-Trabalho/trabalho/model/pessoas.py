class Pessoa:
    __id = 0
    __nome = ''
    __sobrenome = ''
    __identidade = 0
    
    #getter
    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome
    
    def get_identidade(self):
        return self.__identidade
    
    #setters

    def set_nome(self, nome):
        self.__nome = nome

    def set_sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome
    
    def set_identidade(self, identidade):
        self.__identidade = identidade
        



