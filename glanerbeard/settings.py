import sys

class Settings:
    def init(self, app):
        app.config.from_object('glanerbeard.default_settings')
        app.config.from_envvar('GLANERBEARD_SETTINGS')
        self.app = app

    def __getitem__(self, item):
        return self.app.config[item]

sys.modules[__name__] = Settings()
