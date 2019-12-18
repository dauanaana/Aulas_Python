import sys
sys.path.append("C:/Users/hbsis/Desktop/Dauana/AulasPythonClt2/trabalho/")
from model.pessoas import Pessoa


class Funcionario(Pessoa):

    __cargo = ''
    __salario = ''


    #getters

    def get_salario(self):
        return self.__salario

    def get_cargo(self):
        return self.__cargo
    
        
    #setters

    def set_salario(self, salario):
        self.__salario = salario

    def set_cargo(self, cargo):
        self.__cargo = cargo
    



        
