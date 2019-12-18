import sys
sys.path.append("C:/Users/hbsis/Desktop/Dauana/AulasPythonClt2/trabalho/")
from flask import Flask, render_template, request, redirect
from dao.funcionario_dao import FuncionarioDao
from dao.equipe_dao import EquipeDao
from dao.linguagens_dao import LinguagensDao


app = Flask(__name__)

##***** litagem
@app.route('/')
def iniciar():
    return render_template('home.html')

@app.route('/listagem_funcionarios')
def listar_func():
    func = FuncionarioDao()
    listar = func.listar()
    return render_template('listagem.html', func = listar)


@app.route('/listagem_equipes')
def listar_equip():
    equip = EquipeDao()
    listar = equip.listar()
    return render_template('listagem.html', equip = listar)


@app.route('/listagem_linguagens')
def listar_ling():
    ling = LinguagensDao()
    listar = ling.listar()
    return render_template('listagem.html', ling = listar)

##**** cadastrar
@app.route('/cadastrar_funcionarios')
def cadastrar_func():
   return render_template('cadastro.html')

@app.route('/cadastrar_equipes')
def cadastrar_equip():
    return render_template('cadastro.html')

@app.route('/cadastrar_linguagens')
def cadastrar_ling():
    return render_template('cadastro.html')



##******** salvar
@app.route('/salvar_funcionarios', methods = ['POST'])
def salvar_func():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    identidade = request.form['identidade']
    cargo = request.form['cargo']
    salario = request.form['salario']
    func = FuncionarioDao()
    func.inserir(nome, sobrenome, identidade, cargo, salario)
    return redirect('/')

@app.route('/salvar_equipe', methods = ['POST'])
def salvar_equip():
   nome_equipe = request.form['nome_equipe']
   equip = EquipeDao()
   equip.inserir(nome_equipe)
   return redirect('/')

@app.route('/salvar_linguagens', methods = ['POST'])
def salvar_ling():
   tipolinguagem = request.form['tipolinguagem']
   ling = LinguagensDao()
   ling.inserir(tipolinguagem)
   return redirect('/')

##**********  deletar
@app.route('/deletar_funcionario')
def deletar_func():
    id = request.args['id']
    func = FuncionarioDao()
    func.deletar(id)
    return redirect('listagem.html')

@app.route('/deletar_equipes')
def deletar_equip():
    id = request.args['id']
    equip = EquipeDao()
    equip.deletar(id)
    return redirect('listagem.html')

@app.route('/deletar_linguagens')
def deletar_ling():
    id = request.args['id']
    ling = LinguagensDao()
    ling.deletar(id)
    return redirect('listagem.html')

app.run(port=80, debug=True)



