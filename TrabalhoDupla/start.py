from flask import Flask, render_template, request, redirect
from pessoa import Pessoa
from funcionario_dao import FuncionarioDAO

#------ iniciar flask

app = Flask(__name__)

#------ listar cadastrados

@app.route('/')
def listagem():
    opt = FuncionarioDAO()
    lista = opt.listar()
    return render_template('listagem.html', lista = lista)

#------ cadastrar funcionarios

@app.route('/cadastrar')
def form_cadastrar():
    return render_template('formulario.html')

#------ editar cadastros

@app.route('/editar')
def editar():
    id = request.args['id']
    funcionario_dao = FuncionarioDAO()
    pessoa = funcionario_dao.buscar_por_id(id)
    return render_template('editar.html', pessoa = pessoa)

#------ salvar cadastros

@app.route('/salvar', methods = ['POST'])
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    identidade = request.form['identidade']
    funcionario_dao = FuncionarioDAO()
    funcionario_dao = pessoa.cadastar(nome, sobrenome, identidade)
    return redirect('/')

#------ salvar e editar cadastros

@app.route('/salvar_editar', methods=['POST'])
def editar_salvar():
    id = request.form['id']
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    identidade = request.form['identidade']
    pessoa = Pessoa(nome, sobrenome, identidade, id)
    funcionario_dao = FuncionarioDAO()
    funcionario_dao.alterar(pessoa)
    return redirect('/')

app.run(port=80, debug=True)
