from flask import Flask
import app.menu as menu

app = Flask(__name__)

@app.route("/")
def index():
    resultado = menu.exibir_menu()
    return resultado

if __name__ == "__main__":
    app.run(debug=True)
