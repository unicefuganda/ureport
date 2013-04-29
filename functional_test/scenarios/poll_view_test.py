from nose.tools import assert_equal
from nose.tools import assert_true

from fixtures.create_poll_utils import simulate_response
from fixtures.create_polls_for_view_poll import  create_polls
from fixtures.home_page import HomePage


class TestPollView():

    @classmethod
    def setUpClass(cls):
        cls.home_page = HomePage().load()
        pass

    @classmethod
    def tearDownClass(cls):
        cls.home_page.close_page()

    def test_that_poll_list_is_present(self):
        polls = create_polls(11)
        for poll in polls:
            poll.start()

            lastResponseText = 'yes'
            for contact in poll.contacts.all():
                responseText = 'yes' if (lastResponseText == 'no') else 'no'
                lastResponseText = responseText
                simulate_response(contact.default_connection, responseText)

            assert(poll.messages.count() > 0)
            poll.end()
        assert_true(True)
