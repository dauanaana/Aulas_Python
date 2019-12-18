import MySQLdb
from dao.frutas_dao import FrutasDao
from dao.legumes_dao import LegumesDao
from dao.verduras_dao import VerdurasDao


from model.frutas_model import Frutas
from model.legumes_model import Legumes
from model.verduras_model import Verduras

lista = [
    ['frutas','verduras','legumes','preço'],
    ['mamão','abacaxi','laranja','uva','pera','maçã','vergamota'],
    ['alface crespa', 'alface lisa','rucula','almeirão','repolho','salsinha','couve'],
    ['feijão', 'ervinha', 'lentilha','vagem','feijão branco','grão de bico','soja'],
    [ 
        [10.00, 2.56, 5.25, 9.5, 10.05, 15, 5.75],
        [2.99, 2.95, 3.5, 3.25, 5.89, 2.9, 2.5],
        [9.0, 5.0, 7.5, 1.75, 10.9, 5.99, 3.55] 
    ]
]


dao_fruta = FrutasDao()
dao_verdura = VerdurasDao()
dao_legume = LegumesDao()
##########listar do banco
def listar_frutas():
    print('FRUTAS: ')
    for l in dao_fruta.listar():
        print(f"{l['nome']} : {l['preco']}")

def listar_legumes():
    print('LEGUMES: ')
    for l in dao_legume.listar():
        print(f"{l['nome']} : {l['preco']}") 

def listar_verduras():
    print('VERDURAS: ')
    for l in dao_verdura.listar():
        print(f"{l['nome']} : {l['preco']}")

##############inserir no banco
def inserir_no_banco():
    #Fruta
    for i in range(7):
        fruta = Frutas(lista[1][i], lista[4][0][i])
        dao_fruta.inserir(fruta)

    #Legume
    for i in range(7):
        legume = Legumes(lista[3][i], lista[4][2][i])
        dao_legume.inserir(legume)

    #Verdura
    for i in range(7):
        verdura = Verduras(lista[2][i], lista[4][1][i])
        dao_verdura.inserir(verdura)



# inserir_no_banco()


while True:

    print('********************\n')
    print("1 = FRUTAS")
    print("2 = LEGUMES")
    print("3 = VERDURAS\n")

####tratamento de erros
    try:
        opcao = int(input('Escolha uma opção: '))
    except:
        print('Opcão Inválida!!!')
    else:
        if opcao == 1:
            listar_frutas()
        elif opcao == 2:
            listar_legumes()
        elif opcao == 3:
            listar_verduras()
        else:
            break








# listar_frutas()

