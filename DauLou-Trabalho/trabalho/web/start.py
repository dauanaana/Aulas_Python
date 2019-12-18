import sys
sys.path.append("C:/Users/hbsis/Desktop/DauLou-Trabalho-master/trabalho/")

from flask import Flask, render_template, request, redirect

from dao.funcionario_dao import FuncionarioDao
from dao.equipe_dao import EquipeDao
from dao.linguagens_dao import LinguagensDao

from model.funcionario import Funcionario
from model.equipe import Equipe
from model.linguagens import Linguagem


app = Flask(__name__)


@app.route('/')
def iniciar():
    return render_template('home.html')

##***** listagem
@app.route('/funcionarios')
def listar_funcionario():
    # title = 'Funcionarios'
    func = FuncionarioDao()
    lista = func.listar()
    return render_template('lista_funcionarios.html', lista = lista)


@app.route('/equipes')
def listar_equipe():
    # title = 'Equipes'
    equip = EquipeDao()
    lista = equip.listar()
    return render_template('lista_equipes.html', lista = lista)


@app.route('/linguagens')
def listar_linguagem():
    # title = 'Linguagem'
    ling = LinguagensDao()
    lista = ling.listar()
    return render_template('lista_linguagens.html', lista = lista)

##**** formularios cadastrar
@app.route('/form_funcionario')
def cadastrar_funcionario():
    return render_template('form_funcionario.html')

@app.route('/form_equipe')
def cadastrar_equipe():
    return render_template('form_equipe.html')

@app.route('/form_linguagem')
def cadastrar_linguagens():
    return render_template('form_linguagem.html')



##******** salvar
@app.route('/salvar_funcionario', methods = ['POST'])
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
   nome_equipe = request.form['nome']
   nome_linguagem = request.form['linguagem']
   equip = EquipeDao()
   equip.inserir(nome_equipe, nome_linguagem)
   return redirect('/')

@app.route('/salvar_linguagem', methods = ['POST'])
def salvar_ling():
   tipolinguagem = request.form['nome']
   ling = LinguagensDao()
   ling.inserir(tipolinguagem)
   return redirect('/')

#**********  deletar
@app.route('/deletar_funcionario')
def deletar_func():
    id = request.args['id']
    func = FuncionarioDao()
    func.deletar(id)
    return redirect('/funcionarios')

@app.route('/deletar_equipe')
def deletar_equip():
    id = request.args['id']
    equip = EquipeDao()
    equip.deletar(id)
    return redirect('/equipes')

@app.route('/deletar_linguagem')
def deletar_ling():
    id = request.args['id']
    ling = LinguagensDao()
    ling.deletar(id)
    return redirect('/linguagens')

app.run(port=80, debug=True)



