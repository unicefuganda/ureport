from ureport.tasks import ping
from nose.tools import assert_equal

class TestPing():

    @classmethod
    def setup_class(klass):
        print "Setup at the class..."

    @classmethod
    def teardown_class(klass):
        print "Teardown at the class.."

    def setUp(self):
        print "Setup..."

    def teardown(self):
        print "Teardown..."
        

    def test_ping_synchronous(self):
        result = ping()
        assert_equal(result, "pong")

    def test_ping_asynchronous(self):
        result = ping.delay()
        while result.ready() != True:
            print "Waiting 0.5 secs for a result..."
            import time
            time.sleep(0.5)

            print "Got a result!"
            print "Result was [" + str(result.info) + "]"
        
        assert_equal("pong", str(result.info))
