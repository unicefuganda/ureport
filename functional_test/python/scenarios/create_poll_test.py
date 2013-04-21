from fixtures.ureport_context import init_ureport_env

class TestNoseExamples():

    @classmethod
    def setup_class(klass):
        print "Setup at the class.."

    @classmethod
    def teardown_class(klass):
        print "Teardown at the class.."

    def setUp(self):
        print "Setup..."

    def teardown(self):
        print "Teardown..."
        

    def test_something(self):
        print "Everything is ok!"
