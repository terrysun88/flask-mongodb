from flask import Flask
from app import api
from app.database import initialize_db

def create_app():
	app = Flask(__name__)
	app.register_blueprint(api.routes.blueprint)

	app.config['MONGODB_SETTINGS'] = {
	 'host': 'mongodb://localhost/film_rental'
	}

	initialize_db(app)

	return app