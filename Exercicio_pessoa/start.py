from pessoa import Pessoa




def criar_lista():

    pess = [
            ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
            ]
        
    lista_pessoa_maior = []
    lista_pessoa_menor = []

    for i in range(7):
        l_pessoa = []
        for n in range(4):
            l_pessoa.append(pess[n][i])
        pessoa = Pessoa(l_pessoa[0], l_pessoa[1], l_pessoa[2], l_pessoa[3])               
        if int(l_pessoa[3]) >= 18:
            lista_pessoa_maior.append(pessoa)
        else:
            lista_pessoa_menor.append(pessoa)

    return [lista_pessoa_maior, lista_pessoa_menor]
    

listas = criar_lista()

for lista in listas:
    print('='*40)
    for i in lista:
        print(i.nome)
        print(i.telefone)
        print(i.email)
        print(i.idade)
    

    