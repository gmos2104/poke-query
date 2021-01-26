######
Docker
######

This project can be run using docker.

==============
Pre-Requisites
==============

- docker

======
Set up
======

#. Create a ``.env`` file.

   ``cp .env-template .env``

#. Build the docker image:

   ``docker build -t poke-query:development .``

===================
Running the Project
===================

Start container:

  ``./run-docker.sh``

==============
Other Commands
==============

- Stop container: ``docker stop poke-query``
- View container logs: ``docker logs poke-query``
