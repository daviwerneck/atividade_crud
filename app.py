# verifico a pasta do meu projeto, verifico se está no meu github
# git remote -v
# e executo
# git pull origin master
# quero clonar o projeto
# git clone https://...
# instalo a extensao python
# abro o terminal e verifico se abre no venv, caso não abra, eu devo executar
# ctrl shift p
# e digitar envrironment e pedir para criar um ambiente virtual
# pip install flask
# pip install Flask-SQLAlchemy
# pip install Flask-Migrate
# pip install Flask-Script
# pip install pymysql

# flask db init
# flask db migrate -m "Migração Inicial"
# flask db upgrade
# flask run --debug

from flask import Flask, render_template, request, flash, redirect
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Fornecedor
app.config['SECRET_KEY'] = 'cd6ec8a03ee6252de83e921bd4be5e016819ed51221599fea40e5cbfd110ecce'

# drive://usuario:senha@servidor/banco_de_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/flaskg2"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dados', methods=['POST'])
def dados():
    flash('Dados enviados!!')
    dados = request.form
    return render_template('dados.html', dados=dados)

@app.route('/fornecedor')
def fornecedor():
    f = Fornecedor.query.all()
    return render_template('fornecedor_lista.html', dados = f)

@app.route('/fornecedor/add')
def fornecedor_add():
    return render_template('fornecedor_add.html')

@app.route('/fornecedor/save', methods=['POST'])
def fornecedor_save():
    nome = request.form.get('nome')
    contato = request.form.get('contato')
    cidade = request.form.get('cidade')
    if nome and contato and cidade:
        fornecedor = Fornecedor(nome, contato, cidade)
        db.session.add(fornecedor)
        db.session.commit()
        flash('Fornecedor cadastrado com sucesso!!!')
        return redirect('/fornecedor')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/fornecedor/add')

@app.route('/fornecedor/remove/<int:id_fornecedor>')
def fornecedor_remove(id_fornecedor):
    fornecedor = Fornecedor.query.get(id_fornecedor)
    if fornecedor:
        db.session.delete(fornecedor)
        db.session.commit()
        flash('Fornecedor removido com sucesso!!!')
        return redirect('/fornecedor')
    else:
        flash('Caminho incorreto!!!')
        return redirect('/fornecedor')
    
@app.route('/fornecedor/edita/<int:id_fornecedor>')
def fornecedor_edita(id_fornecedor):
    fornecedor = Fornecedor.query.get(id_fornecedor)
    return render_template('fornecedor_edita.html', dados = fornecedor)

@app.route('/fornecedor/editasave', methods=['POST'])
def fornecedor_editasave():
    nome = request.form.get('nome')
    contato = request.form.get('contato')
    cidade = request.form.get('cidade')
    id_fornecedor = request.form.get('id_fornecedor')
    if id_fornecedor and nome and contato and cidade:
        fornecedor = Fornecedor.query.get(id_fornecedor)
        fornecedor.nome = nome
        fornecedor.contato = contato
        fornecedor.cidade = cidade
        db.session.commit()
        flash('Dados atualizados com sucesso!!!')
        return redirect('/fornecedor')
    else:
        flash('Faltando dados!!!')
        return redirect('/fornecedor')


if __name__ == '__main__':
    app.run()
