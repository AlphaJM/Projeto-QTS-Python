from flask import Flask, render_template, request
from menu import exibir_menu_admin, exibir_menu, main
import cadastro

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Página inicial do seu aplicativo

@app.route("/menu")
def mostrar_menu():
    exibir_menu()  # Chama a função para exibir o menu
    return "Menu exibido com sucesso!"

@app.route("/menu_admin")
def mostrar_menu_admin():
    exibir_menu_admin()  # Chama a função para exibir o menu de administração
    return "Menu de administração exibido com sucesso!"

@app.route("/processar_opcao_admin", methods=["POST"])
def processar_opcao_admin():
    opcao = request.form["opcao_admin"]  # Obtém a opção escolhida pelo usuário
    if opcao == "1":
        titularidade = request.form['titularidade']
        cadastro.cadastrar_titularidade(titularidade)
    elif opcao == "2":
        nome = request.form['nome']
        especializacao = request.form['especializacao']
        codigo_lattes = request.form['codigo_lattes']
        id_titularidade = request.form['id_titularidade']
        cadastro.cadastrar_professor(nome, especializacao, codigo_lattes, id_titularidade)
    return "Opção do menu de administração processada com sucesso!"

if __name__ == "__main__":
    app.run(debug=True)
