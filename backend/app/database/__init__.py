from flask_mongoengine import MongoEngine

db_engine = MongoEngine()

def initialize_db(app):
    db_engine.init_app(app)