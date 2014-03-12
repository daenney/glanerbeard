###########
Glanerbeard
###########

Tool to bridge multiple Sickbeards into one interface.

Development
===========

Install:

.. code-block:: bash

   $ pip install -r requirements.txt

Run development server (bash/zsh):

.. code-block:: bash

   $ GLANERBEARD_SETTINGS=/path/to/$custom_settings.py python dev.py

Run development server (fish):

.. code-block:: bash

   $ env GLANERBEARD_SETTINGS=/path/to/$custom_settings.py python dev.py

The environment variable ``GLANERBEARD_SETTINGS`` must point to a file
identical in markup to ``glanerbeard/default_settings.py`` and override/set
the required keys. You must at least provide ``API_KEYS`` and ``SERVERS``,
probably also change ``LOGLEVEL``.
