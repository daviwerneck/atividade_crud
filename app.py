from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.config['SECRET_KEY'] = 'cd6ec8a03ee6252de83e921bd4be5e016819ed51221599fea40e5cbfd110ecce'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aula')
@app.route('/aula/<nome>')    
@app.route('/aula/<nome>/<curso>')
@app.route('/aula/<nome>/<curso>/<int:ano>')
def aula(nome = 'João', curso = 'Informática', ano = 1):
    dados = {'nome':nome, 'curso':curso, "ano":ano}
    return render_template('aula.html', dados_curso = dados)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados', methods=['POST'])
def dados():
    flash('Dados enviados!!')
    dados = request.form
    return render_template('dados.html', dados=dados)

if __name__ == '__main__':
    app.run()
