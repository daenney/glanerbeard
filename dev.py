from glanerbeard.web import app
from glanerbeard.default_settings import DEV_LISTEN_HOST, DEV_LISTEN_PORT

if __name__ == '__main__':
	app.debug = True
	app.run(DEV_LISTEN_HOST, DEV_LISTEN_PORT)
