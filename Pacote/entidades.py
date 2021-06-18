from Pacote import db, loginmanager
from flask_login import UserMixin
from datetime import datetime



class usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(10), nullable = False)

    cadastrodebikes = db.relationship('cadastrodebikes', backref='usuario', lazy=True)

class cadastrodebikes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Model = db.Column(db.String(100), nullable = False)
    Modality = db.Column(db.String(20), nullable = False)
    Gender = db.Column(db.String(20), nullable = False)
    Suspensao = db.Column(db.String(30), nullable = False)
    Aro = db.Column(db.String(20), nullable = False)
    Marchas = db.Column(db.String(20), nullable = False)
    Marca = db.Column(db.String(30), nullable = False)
    Price = db.Column(db.String(20), nullable = False)
    img_bicicleta = db.Column(db.String(100), default="")

    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable = False)
    alugueldebikes = db.relationship('alugueldebikes', backref='cadastrodebikes', lazy=True)

class alugueldebikes(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     Address = db.Column(db.String(100), nullable = False)
     City = db.Column(db.String(20), nullable = False)
     State = db.Column(db.String(50), nullable = False)
     CEP = db.Column(db.String(9), nullable = False)
     DataRetirada = db.Column(db.DateTime(20), nullable = False)
     HoraRetirada = db.Column(db.Time(20), nullable = False)
     DataDevolucao =db.Column(db.DateTime(20), nullable = False)
     HoraDevolucao =db.Column(db.Time(20), nullable = False)

     id_cadastrodebikes = db.Column(db.Integer, db.ForeignKey("cadastrodebikes.id"), nullable = False)
