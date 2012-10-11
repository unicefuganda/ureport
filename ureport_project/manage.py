#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from django.core.management import execute_manager
import settings
import eventlet
import eventlet.debug
import os
#patch for eventlet
os.environ["EVENTLET_NOPATCH"] = 'True'
eventlet.monkey_patch()
eventlet.debug.hub_prevent_multiple_readers(False)

if __name__ == "__main__":
    execute_manager(settings)
