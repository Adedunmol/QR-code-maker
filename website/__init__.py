from flask import Flask
from flask_qrcode import QRcode

qrcode = QRcode()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'bdhgyuefueecyaajwdbs'

    qrcode.init_app(app)

    from website.home import home

    app.register_blueprint(home)

    return app

