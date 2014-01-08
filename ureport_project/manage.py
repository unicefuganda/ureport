#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    """
    you can add something like this here:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.production")

    but its better to set the environment variable with a deploy script

    and just pass --settings=settings.dev to manage.py when running locally
    """

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
