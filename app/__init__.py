from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importar e registrar blueprints
    from .routes.gerar_horario import gerar_horario_bp
    from .routes.cadastro import cadastro_bp
    app.register_blueprint(gerar_horario_bp)
    app.register_blueprint(cadastro_bp)

    return app