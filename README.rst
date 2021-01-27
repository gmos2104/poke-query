##########
Poke-Query
##########

API that adds query improvements to the great `PokéApi <https://pokeapi.co>`_

This app is part of a coding challenge.

See `Project Requirements <docs/requirements.rst>`_.

==============
Pre-Requisites
==============

- Python 3.8
- Have a running Redis instance.

======
Set Up
======

1. Create a virtual environment on a directory of choice:

  ``python3 -m venv .venv``

2. Activate virtualenv:

  ``. .venv/bin/activate``

3. Install dependencies:

  ``pip install -r requirements/development.txt``

4. Create a ``.env`` file from template example:

   ``cp .env-template .env``

===================
Running the Project
===================

Start the development server run:

  ``flask run``

To run the tests:

  ``python -m pytest --cov=api``

=============
Documentation
=============

Aditional documentation can be found in the ``docs`` folder.

Proyect also uses OpenAPI and Swagger UI to document the API's. The docs can be viewed in ``localhost:5000/docs/``

======
Docker
======

Project can be run using docker. See Docker_ for more details.

.. _Docker: docs/docker.rst
