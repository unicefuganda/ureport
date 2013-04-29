from nose.tools import assert_equal
from nose.tools import assert_true

from fixtures.create_polls_for_view_poll import  create_and_start_polls
from fixtures.home_page import HomePage, UreportApplication


class TestPollView():

    def setUp(self):
        self.ureport_application = UreportApplication()

    def tearDown(self):
        self.ureport_application.close()

    def test_that_there_should_be_only(self):
        expected_number_of_polls = 10 # TODO load this from the settings

        create_and_start_polls(expected_number_of_polls + 1)

        home_page = self.ureport_application.navigate_to_home_page()

        assert_equal(expected_number_of_polls, home_page.number_of_previous_polls())


