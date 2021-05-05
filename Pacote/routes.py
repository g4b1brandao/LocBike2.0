from flask import current_app as app, render_template, request



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
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrodebicicletas")
def cadastrodebicicletas():
    return render_template("cadastrodebicicletas.html")

