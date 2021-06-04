from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
db = SQLAlchemy()
loginmanager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    #app.config['DEBUG'] = True
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://LocBike:12a34b56c@LocBike.mysql.pythonanywhere-services.com/LocBike$teste'
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config.from_object('config')
    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path,'uploads')

    app.secret_key = '12032021'

    db.init_app(app)
    loginmanager.init_app(app)


    with app.app_context():
        from . import routes
        from . import entidades

    return app

