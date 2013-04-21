from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

class TestNoseExamples():

    @classmethod
    def setup_class(klass):
        """This method is run once for each class before any tests are run"""    

    @classmethod
    def teardown_class(klass):
        """This method is run once for each class _after_ all tests are run"""    

    def setUp(self):
        """This method is run once before _each_ test method is executed"""    

    def teardown(self):
        """This method is run once after _each_ test method is executed"""    

    def test_equals(self):
        assert_equal("Some Value", "Some Value")
        assert_not_equal("something else", "Incorrect Value")    

    def test_boolean(self):
        assert_equal(True, True)
        assert_not_equal(True, False)    

    @raises(Exception)
    def test_raise_exc_with_decorator(self):
        raise(Exception("A message"))
