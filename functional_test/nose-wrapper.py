#!/usr/bin/python
# EASY-INSTALL-ENTRY-SCRIPT: 'nose==1.3.0','console_scripts','nosetests'
__requires__ = 'nose==1.3.0'
import sys
from pkg_resources import load_entry_point

from fixtures.ureport_context import init_ureport_env

init_ureport_env()

print "----------------------------------------------------------------------\n"

sys.exit(
   load_entry_point('nose==1.3.0', 'console_scripts', 'nosetests')()
)
