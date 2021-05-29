from flask import current_app as app, render_template, request, redirect
from Pacote import db, loginmanager
from Pacote.entidades import usuario , cadastrodebikes

from flask_login import login_user, logout_user, login_required


loginmanager.login_view = '/login'

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
            return redirect('/login')
    # quando for GET enviar o template.
    return render_template("cadastro.html")

@app.route('/login')
def login():
       return render_template("login.html")



@app.route('/login_tent', methods=['POST'])
def login_tent ():
        email_log = request.form ['email']
        senha_log = request.form ['senha']

        tem = usuario.query.filter_by(email=email_log).first()

        if tem is None:
            return 'Usuário não existe'
        else:
           if tem.password == senha_log:
               return render_template('catalogo.html')

@app.route("/cadastrodebicicletas", methods=['GET', 'POST'])
def cadastrodebicicletas():
    if request.method == 'POST':
        enderecoderetirada = request.form ['Address']
        Cidade = request.form ['Cidade']
        estado = request.form ['Estado']
        cep = request.form ['CEP']
        modelo = request.form ['Modelo']
        modalidade = request.form ['Modalidade']
        aro_e_machas = request.form ['Aro_e_Machas']

        novo = cadastrodebikes()
        novo.Address = enderecoderetirada
        novo.Cidade =  Cidade
        novo.estado = estado
        novo.cep = cep
        novo.modelo = modelo
        novo.modalidade = modalidade
        novo.aro_e_machas = aro_e_machas

        db.session.add(novo)
        db.session.commit()
        novo.usuario_id = login_user.id
        return redirect('/teste2')
    return render_template("cadastrodebicicletas.html")




@app.route("/teste", methods=['POST'])
def teste():
    return render_template("teste.html")

@app.route("/teste2")
def teste2():
    return render_template("teste2.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@loginmanager.user_loader
def load_user(user_id):
    return usuario.query.get(user_id)