from Pacote import db


class usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(50), nullable = False)
    lastname = db.Column(db.String(50), nullable = False)
    password = db.Column(db.String(10), nullable = False)

#    def __init__(self,name,lastname,password,email):
#        self.name = name
#        self.lastname = lastname
#        self.email = email
#        self.password = password


