from ci_settings import *
TEST_RUNNER = 'runner.NoDbTestRunner'
#If you just want to see the coverage for the functional tests '--cover-erase' - otherwise it adds to the unit test
NOSE_ARGS = ('--with-xunit', '--xunit-file=target/reports/functional-test/nosetests.ureport.xml', 
             '--with-coverage', '--cover-html', '--cover-html-dir=target/reports/functional-test/coverage', '--cover-package=ureport_project,poll,uganda_common,unregister,message_classifier,contact')

