#!/usr/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'nose==0.11.4','console_scripts','nosetests'
__requires__ = 'nose==0.11.4'
import sys
from pkg_resources import load_entry_point

from fixtures.ureport_context import init_ureport_env

init_ureport_env()

print "----------------------------------------------------------------------\n"

sys.exit(
   load_entry_point('nose==0.11.4', 'console_scripts', 'nosetests')()
)
