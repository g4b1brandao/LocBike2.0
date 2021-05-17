from Pacote import db

class usuario(db.Model):
 id = db.Column(db.Integer, primary_key = True)
 email = db.Column(db.String(100), nullable=False, unique=True)
 nome = db.Column(db.String(50), nullable = False)
 sobrenome = db.Column(db.String(50), nullable = False)
 senha = db.Column(db.String(10), nullable = False)

