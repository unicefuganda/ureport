import os,sys
from django.core.management import setup_environ


def init_ureport_env():
    ureportProject = os.environ['UREPORT_HOME'] + "/ureport_project" 

    print "\nInitialising environment for functional tests...\n" 

    print "ureport is in [" + ureportProject + "]"
    print "Using settings [ci_settings]\n"


    sys.path.insert(0,ureportProject) 
    import ci_settings

    setup_environ(ci_settings)

    import djcelery
    djcelery.setup_loader()
    
    print "\nuReport environment initialised.\n"
