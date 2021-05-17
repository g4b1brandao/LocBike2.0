from flask import Flask
import click
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://LocBike:12a34b56c@LocBike.mysql.pythonanywhere-services.com/LocBike$teste'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.cli.add_command(cm_db)

    with app.app_context():
        from . import routes

    return app

@click.command('cm-db')
@with_appcontext
def cm_db():
    from . import entidades
    db.create_all()
    print('Criado com sucesso')