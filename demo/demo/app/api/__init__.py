from flask import Flask
from flask_cors import CORS


def create_app():
    """
    Create a flask instance here.
    """
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, supports_credentials=True)

    from app.api.hello import hello_blueprint

    # register the blueprints
    app.register_blueprint(hello_blueprint, url_prefix='/greeting')

    return app
