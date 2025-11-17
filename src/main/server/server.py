from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

# Importar Blueprint
from src.main.routes.pets_routes import pet__route_bp
from src.main.routes.person_routes import person_route_db

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet__route_bp)
app.register_blueprint(person_route_db)