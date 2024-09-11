from database import db

class Fornecedor(db.Model):
    __tablename__="fornecedor"
    id_fornecedor = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    contato = db.Column(db.String(100))
    cidade = db.Column(db.String(50))

    def __init__(self, nome, contato, cidade):
        self.nome = nome
        self.contato = contato
        self.cidade = cidade

    def __repr__(self):
        return "<Fornecedor {}>".format(self.nome)