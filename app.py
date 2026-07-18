"""
Punto de entrada de la aplicación SISSU - UNAD.
Usa el patrón application factory: create_app() ensambla la app a partir
de sus blueprints (rutas) y la base de datos.
"""
from flask import Flask
from dotenv import load_dotenv

from config import Config
from database.connection import init_db
from routes.main_routes import main_bp
from routes.api_routes import api_bp

load_dotenv()  # carga variables desde .env en desarrollo local


def create_app() -> Flask:
    app = Flask(__name__)

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)

    with app.app_context():
        init_db()

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=Config.PORT, debug=False)
