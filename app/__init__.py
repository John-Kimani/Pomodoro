from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()


def create_app(config_name):
    '''
    Factory function
    '''
    app = Flask(__name__)


    '''
    Create app config
    '''
    app.config.from_object(config_options[config_name])

    '''
    Initializing bootstrap
    '''
    bootstrap.init_app(app)

    '''
    Registering main
    '''
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    

    return app