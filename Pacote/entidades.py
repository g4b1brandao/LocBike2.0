from Pacote import db, loginmanager
from flask_login import UserMixin


class usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(10), nullable = False)

    cadastrodebikes = db.relationship('cadastrodebikes', backref='usuario', lazy=True)

class cadastrodebikes(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Address = db.Column(db.String(100), nullable = False)
    City = db.Column(db.String(20), nullable = False)
    State = db.Column(db.String(50), nullable = False)
    CEP = db.Column(db.String(9), nullable = False)
    Model = db.Column(db.String(100), nullable = False)
    Modality = db.Column(db.String(20), nullable = False)
    Aro_e_Machas = db.Column(db.String(20), nullable = False)
    img_bicicleta = db.Column(db.String(100), default="")

    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable = False)