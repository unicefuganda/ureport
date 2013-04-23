import datetime
from django.contrib.auth.models import User
from django_liveserver.testcases import LiveServerTestCase


class SplinterTestCase(LiveServerTestCase):
    def __init__(self, methodName='runTest'):
        super(SplinterTestCase, self).__init__(methodName)

    def follow_link(self, text):
        (self.browser.find_element_by_link_text(text)).click()


    def select_by_text(self, name, text):
        self.browser.find_by_xpath(
            '//select[@name="%s"]/option[normalize-space(.)="%s"]' % (name, text)).first._element.click()


    def create_and_sign_in_admin(self,username,password):
        admin_user = User.objects.create_superuser(username, 'admin@test.com', password)
        self.open('/accounts/login')
        self.browser.fill("username", username)
        self.browser.fill("password", password)
        self.browser.find_by_css("input[type=submit]").first.click()


    def open(self, url):
        self.browser.visit("%s%s" % (self.live_server_url, url))

    def wait_for_seconds(self, time_out_in_seconds):
        current_time = datetime.datetime.now()
        end_time = current_time + datetime.timedelta(0, time_out_in_seconds)

        while current_time < end_time:
            current_time = datetime.datetime.now()
