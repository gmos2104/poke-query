#####
Notes
#####

- Since PokéAPI does not support filtering pokémons retrieved by name and the results returned are ordered by their ID and not by name my solution was to pull all pokémons in a single query (the endpoint just returns name and a link so they hold minimal data per entry). Then the name filtering is done by a simple `contains` check ``if q in name``.

- Both endpoints save their results on a redis cache the first time they query a resource to avoid hitting the PokéAPI service many times.

- Since I use the assignment expressions (with the walrus operator ``:=``) in various parts of the application the minimum Python version required to run it is 3.8

- API's are documented using the OpenAPI spec with the Swagger UI for visualization.

- Code formatting is done using `black <https://github.com/psf/black>`_.

- Testing is done using the `pytest <https://docs.pytest.org/en/stable/index.html>`_ with the coverage pluggin.
