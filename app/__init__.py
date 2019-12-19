from flask import Flask
import os
from instance.config import app_config

def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True,static_url_path='/static')
    app.config.from_object(app_config[config_name]())
    #app.config['SQLALCHEMY_DATABASE_URI'] = os.path.join(app.instance_path, 'app.db')
    app.config['DATABASE'] = os.path.join(app.instance_path, 'app.db')

    return app

