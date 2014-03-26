from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from glanerbeard import factory

application = DispatcherMiddleware(factory.create_app('glanerbeard'))

if __name__ == "__main__":
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
