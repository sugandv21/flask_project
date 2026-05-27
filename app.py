from flask import Flask

from flask_restful import Api

from flask_cors import CORS

from config import Config

from extensions import db

from routes import initialize_routes


def create_app():

    app = Flask(__name__)

    # Config
    app.config.from_object(Config)

    # Enable CORS
    CORS(app)
    CORS(app, origins=["http://localhost:3000"])

    # Initialize DB
    db.init_app(app)

    # Initialize API
    api = Api(app)

    # Register Routes
    initialize_routes(api)

    return app


app = create_app()

# Create Tables
with app.app_context():

    db.create_all()


if __name__ == "__main__":

    app.run(debug=True)