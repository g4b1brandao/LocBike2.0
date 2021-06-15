from flask import current_app as app, render_template, request,redirect, session, send_from_directory
from Pacote import db, loginmanager
import os
from werkzeug.utils import secure_filename
from Pacote.entidades import usuario , cadastrodebikes, alugueldebikes

from flask_login import login_user, logout_user, login_required,current_user

from datetime import datetime

loginmanager.login_view = '/login'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def inicio():
	return render_template("index.html")

@app.route('/imagens/<path:filename>')
@login_required
def base_static(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/catalogo", methods=['GET'])
@login_required
def catalogo():
    bicicletas=[1,2,3,4,5,6,7]
    dados = cadastrodebikes.query.all()
    return render_template("catalogo.html", bicicletas=bicicletas,dados=dados)



@app.route("/cadastro" , methods=['GET', 'POST']) # Adicionei método GET
def cadastro():
    if request.method == 'POST': # a parte abaixo só quando for formulário.
        nome = request.form ['name']
        sobrenome = request.form ['lastname']
        email = request.form ['email']
        senha = request.form ['password']
        confirma_senha = request.form ['passconfirmation']

        if (senha == confirma_senha):
            novo = usuario()
            novo.name = nome
            novo.lastname = sobrenome
            novo.email = email
            novo.password = senha


            db.session.add(novo)
            db.session.commit()
            novo.usuario_id = current_user.id
            return redirect('/login')
    # quando for GET enviar o template.
    return render_template("cadastro.html")

@app.route('/login')
def login():
       return render_template("login.html")



@app.route('/login_tent', methods=['POST'])
def login_tent ():
        nome_log = request.form ['name']
        senha_log = request.form ['senha']

        tem = usuario.query.filter_by(name=nome_log).first()

        if tem is None:
            return 'Usuário não existe'
        else:
           if tem.password == senha_log:
               login_user(tem)
               session['user_name'] = nome_log
               return render_template('catalogo.html')

@app.route("/cadastrodebicicletas", methods=['GET', 'POST'])
@login_required
def cadastrodebicicletas():
    if request.method == 'POST':
        enderecoderetirada = request.form ['Address']
        cidade = request.form ['City']
        estado = request.form ['State']
        cep = request.form ['CEP']
        nomedabicicleta = request.form ['Model']
        modalidade = request.form ['Modality']
        genero = request.form ['Gender']
        suspensao = request.form ['Suspensao']
        aro = request.form ['Aro']
        marchas = request.form ['Marchas']
        marca = request.form ['Marca']
        preco = request.form ['Location']

        img_bicicleta = ''
        if 'file' not in request.files:
            session['mensagem'] = 'Não havia arquivo no envio'
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
             session['mensagem'] = 'Não havia arquivo para upload'
             return redirect(request.url)
        if file and allowed_file(file.filename):
             img_bicicleta = secure_filename(file.filename)

             imgs = os.listdir(app.config['UPLOAD_FOLDER'])
             img_bicicleta= f'{len(imgs)+1:08}.{img_bicicleta.rsplit(".", 1)[1].lower()}'

             file.save(os.path.join(app.config['UPLOAD_FOLDER'],img_bicicleta))

        novo = cadastrodebikes()
        novo.Address = enderecoderetirada
        novo.City =  cidade
        novo.State = estado
        novo.CEP = cep
        novo.Model = nomedabicicleta
        novo.Modality = modalidade
        novo.Gender = genero
        novo.Suspensao = suspensao
        novo.Aro = aro
        novo.Marchas = marchas
        novo.Marca = marca
        novo.Price = preco
        novo.img_bicicleta = img_bicicleta
        novo.id_usuario = current_user.id


        db.session.add(novo)
        db.session.commit()

        return redirect('/catalogo')
    return render_template("cadastrodebicicletas.html")



@app.route('/bikesdepasseios')
@login_required
def bikesdepasseios():
       return render_template("bikesdepasseio.html")

@app.route('/bikescasuais')
@login_required
def bikescasuais():
       return render_template("bikescasuais.html")

@app.route('/bikesesportivas')
@login_required
def bikesesportivas():
     return render_template("bikesesportivas.html")

@app.route('/barralateral')
def barralateral():
       return render_template("barralateral.html")


@app.route('/alugar', methods=['GET', 'POST'])
@login_required
def alugar():
     if request.method == 'POST':
        DataRetirada = request.form ['DataRetirada']
        HoraRetirada = request.form ['HoraRetirada']
        DataDevolucao = request.form ['DataDevoluçao']
        HoraRetirada= request.form ['HoraRetirada']


        novo = alugueldebikes()
        novo.DataRetirada = DataRetirada
        novo.HoraRetirada = HoraRetirada
        novo.DataDevolucao =  DataDevolucao
        novo.HoraRetirada = HoraRetirada

        novo.id_cadastrodebikes = current_user.id


        db.session.add(novo)
        db.session.commit()

        return redirect('/catalogo')

     return render_template("alugar.html")


@app.route('/logout')
@login_required
def sair():
    logout_user()
    return redirect('/')

@loginmanager.user_loader
def load_user(user_id):
    return usuario.query.get(user_id)