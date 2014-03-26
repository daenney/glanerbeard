import logging
import os
from flask import Flask

from .core import db
from .frontend import frontend
from . import server
from .helpers import json_print
from .worker import Worker


def create_app(package_name, settings_override=None):
    app = Flask(package_name, instance_relative_config=True)
    app.config.from_object('glanerbeard.default_settings')
    app.config.from_envvar('GLANERBEARD_SETTINGS')
    app.config.from_object(settings_override)

    numeric_level = app.config['LOGLEVEL']
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % numeric_level)
    logging.basicConfig(level=numeric_level)

    db.init_app(app)

    app.register_blueprint(frontend)

    app.jinja_env.filters['json_print'] = json_print

    app.servers = server.from_config(app.config)

    return app

def create_worker(app=None):
    app = app or create_app('glanerbeard', os.path.dirname(__file__))
    worker = Worker(app.config)
    return worker



