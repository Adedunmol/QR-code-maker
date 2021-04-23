from flask import Blueprint, render_template, request, send_file, redirect, url_for

home = Blueprint('home', __name__)


@home.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@home.route('/qrcode', methods=['GET', 'POST'])
def get_qrcode():
    if request.method == 'POST':
        data = request.form.get('url')
    return render_template('code.html', data=data)
