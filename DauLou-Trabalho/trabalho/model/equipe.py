from model.funcionario import Funcionario

class Equipe(Funcionario):
    __nome_equipe = ''

    #getter
    def get_nome_equipe(self):
        return self.__nome_equipe

    # setter
    def set_nome_equipe(self, nome_equipe):
        self.__nome = nome_equipe

