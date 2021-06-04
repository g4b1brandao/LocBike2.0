from flask import current_app as app, render_template, request,redirect, session, url_for
from Pacote import db, loginmanager
import os
from werkzeug.utils import secure_filename
from Pacote.entidades import usuario , cadastrodebikes

from flask_login import login_user, logout_user, login_required,current_user


loginmanager.login_view = '/login'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

bic_mock = [
    {
        "title":"Bicicleta de teste1",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste2",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste3",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste4",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste5",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste6",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste7",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste8",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste9",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste10",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste11",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
    {
        "title":"Bicicleta de teste12",
        "image":"https://static.netshoes.com.br/produtos/bicicleta-de-passeio-kls-retro-aro-26-com-freios-v-brake/54/PAK-0007-154/PAK-0007-154_zoom1.jpg?ts=1616414207&"
    },
]


@app.route("/")
def inicio():
	return render_template("index.html")
@app.route("/catalogo")
@login_required
def catalogo():
    bicicletas=[1,2,3,4,5,6,7]
    return render_template("catalogo.html", bicicletas=bicicletas, bic_mock=bic_mock)

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
        modelo = request.form ['Model']
        modalidade = request.form ['Modality']
        aro_e_machas = request.form ['Aro_e_Machas']

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
        novo.Model = modelo
        novo.Modality = modalidade
        novo.Aro_e_Machas = aro_e_machas
        novo.img_bicicleta = img_bicicleta
        novo.id_usuario = current_user.id


        db.session.add(novo)
        db.session.commit()

        return redirect('/teste2')
    return render_template("cadastrodebicicletas.html")




@app.route("/teste", methods=['POST'])
def teste():
    return render_template("teste.html")

@app.route("/teste2")
def teste2():
    return render_template("teste2.html")

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



@app.route('/logout')
@login_required
def sair():
    logout_user()
    return redirect('/')

@loginmanager.user_loader
def load_user(user_id):
    return usuario.query.get(user_id)