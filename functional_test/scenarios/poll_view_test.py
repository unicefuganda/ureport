from nose.tools import assert_equal
from nose.tools import assert_true

from fixtures.create_polls_for_view_poll import create_and_start_polls
from fixtures.home_page import UreportApplication
from django.conf import settings


class TestPollView():

    def setUp(self):
        self.application = UreportApplication()
        self.set_pagination_limit()

    def tearDown(self):
        self.clear_settings()
        self.application.close()

    def test_that_there_should_be_only_a_limited_number_of_polls_loaded_on_home_page(self):

        expected_number_of_polls = settings.PAGINATION_LIMIT

        create_and_start_polls(expected_number_of_polls + 1)
        home_page = self.application.navigate_to_home_page()

        assert_equal(expected_number_of_polls, home_page.get_number_of_previous_polls())

    def set_pagination_limit(self):
        setattr(settings, 'PAGINATION_LIMIT', 10)

    def clear_settings(self):
        try:
            return delattr(settings, 'PAGINATION_LIMIT')
        except AttributeError:
            pass