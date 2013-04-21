# uReport functional tests

This module contains some standalone functional tests which run against a known server.

If you tell it where the codebase is, it will start up the server and celery for that codebase and then run the functional tests.

At the end of the test run it will shutdown celery and the server.

