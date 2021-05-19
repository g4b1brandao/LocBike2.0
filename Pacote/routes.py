from flask import current_app as app, render_template, request, redirect
from Pacote import db
from Pacote.entidades import usuario



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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':

       return render_template("login.html")


    elif request.method == 'POST':
        raise
        email_log = request.form ['email']
        senha_log = request.form ['password']

        tem = usuario.query.filter_by(email=email_log).first()

        if tem is None:
            return 'Usuário não existe'
        else:
            if tem.senha == senha_log:
                return render_template('teste.html')

@app.route("/cadastrodebicicletas")
def cadastrodebicicletas():
    return render_template("cadastrodebicicletas.html")


@app.route("/teste", methods=['POST'])
def teste():
    return render_template("teste.html")


