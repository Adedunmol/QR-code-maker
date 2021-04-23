from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_qrcode import QRcode

db = SQLAlchemy()
qrcode = QRcode()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bdhgyuefueecyaajwdbs'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///code.db'

    qrcode.init_app(app)
    db.init_app(app)

    from website.home import home

    app.register_blueprint(home)

    create_database(app)

    from website.models import UserUrl

    return app


def create_database(app):
    if not path.exists('website/' + 'code.db'):
        db.create_all(app=app)
        print('Database Created!')
