
aviao = [] 
terminal = ['piloto','oficial1','oficial2','chefe','comissaria1','comissaria2','prisioneiro','policial']

def ir(pessoa1, pessoa2):
    print(f'Pessoas no terminal{terminal}')
    terminal.remove(pessoa1)    
    terminal.remove(pessoa2)
    aviao.append(pessoa1)                 
    aviao.append(pessoa2)
    print(f'Fortwo em movimento, o motorista ({pessoa1}) está levando o passageiro ({pessoa2}) para o avião')

def voltar(pessoa1):
    aviao.remove(pessoa1)
    terminal.append(pessoa1)
    print(f'Pessoas no aviao{aviao}')
    print(f'Fortwo em movimento, o motorista ({pessoa1}) está voltando para o terminal\n')
    






