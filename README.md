# Glanerbeard

Tool to bridge multiple Sickbeards into one interface.

## Development

Install:
```
pip install -r requirements.txt
```

Run development server (bash/zsh):
```
GLANERBEARD_SETTINGS=/path/to/$custom_settings.py python dev.py
```

Run development server (fish):
```
env GLANERBEARD_SETTINGS=/path/to/$custom_settings.py python dev.py
```

The environment variable `GLANERBEARD_SETTINGS` must point to a file identical
in markup to `glanerbeard/default_settings.py` and override/set the required
keys. You must at least provide `API_KEYS` and `SERVERS`, probably also change
`LOGLEVEL`.
