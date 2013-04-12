import re
from django.contrib.auth.models import User, Group
from datetime import datetime
from django_liveserver.testcases import LiveServerTestCase
import psycopg2
from splinter import Browser
import sys
from poll.models import Poll

def create_group(driver, name):
    driver.open('/admin/auth/group/')
    driver.browser.click_link_by_partial_text('Add group')
    driver.browser.fill("name", name)
    driver.browser.find_by_name('_save').first.click()

def create_backend(driver, name):
    driver.open('/admin/rapidsms/backend/')
    driver.browser.click_link_by_partial_text('Add backend')
    driver.browser.fill("name", name)
    driver.browser.find_by_name('_save').click()

def create_contact(driver, name, phone, username, group_name, backend_name):
    driver.open('/admin/rapidsms/contact/')
    driver.browser.click_link_by_partial_text('Add contact')
    driver.browser.fill("name", name)
    driver.select_by_text('user', username)
    driver.select_by_text('groups', group_name)
    driver.browser.fill('birthdate_0', '2013-02-22')
    driver.browser.fill('birthdate_1', '12:55:40')
    driver.select_by_text('gender', 'Male')
    driver.select_by_text('connection_set-0-backend', backend_name)
    driver.browser.fill("connection_set-0-identity", phone)
    driver.browser.find_by_name('_save').click()



class SplinterE2E(LiveServerTestCase):
    def __init__(self, methodName='runTest'):
        super(SplinterE2E, self).__init__(methodName)

    def follow_link(self, text):
        (self.browser.find_element_by_link_text(text)).click()


    def select_by_text(self, name, text):
        self.browser.find_by_xpath(
            '//select[@name="%s"]/option[normalize-space(.)="%s"]' % (name, text)).first._element.click()


    def create_and_sign_in_admin(self,username,password):
        self.open('/accounts/login')
        self.browser.fill("username", username)
        self.browser.fill("password", password)
        self.browser.find_by_css("input[type=submit]").first.click()

    def open(self, url):
        host_and_port = [re.split("=",index)[1] for index in sys.argv if re.match("target_host", index) is not None]
        if not len(host_and_port):
            print "Host and Port not specified. Use ./manage.py test <path_to_test_file> <target_host = x.x.x.x:port_number>\n"
            print "Using: 127.0.0.1:8000 as default host and port configuration"
            host_and_port = ["127.0.0.1:8000"]
        self.browser.visit("%s%s" % ("http://%s" % host_and_port[0], url))

    def wait_for_seconds(self, time_out_in_seconds):
        current_time = datetime.datetime.now()
        end_time = current_time + datetime.timedelta(0, time_out_in_seconds)

        while current_time < end_time:
            current_time = datetime.datetime.now()

BROWSER = Browser('firefox')
class UreportE2ETest(SplinterE2E):

    def setUp(self):
        self.browser = BROWSER
        self.open('/')

    def tearDown(self):
        self.open('/account/logout')

    def create_poll(self,group_name):
        self.open('/createpoll/')
        self.browser.fill("name", "%s" % "foo")
        self.browser.fill("question_en", "bar")
        self.select_by_text('groups', group_name)
        self.browser.find_by_id('createPoll').first.click()

    def should_match_poll_question_to_message_text(self):
        username = "ureport"
        password = "ureport"
        self.create_and_sign_in_admin(username,password)

        group_name="group_name"
        backend_name = "dmark"
        create_backend(self,backend_name)
        create_group(self, group_name)
        create_contact(self, "name", '235454432',username,group_name, backend_name)

        self.create_poll(group_name)

        self.browser.find_link_by_text('Start Poll').first.click()

        assert self.browser.is_text_present('Close Poll')


        connection = psycopg2.connect("dbname=ureport","user=Admin","host=10.48.4.31","password=")
        cursor = connection.cursor()
        sql_text = "select text from rapidsms_httprouter_message where status='Q'"

        cursor.execute(sql_text)
        self.assertEquals(cursor.fetchall().rowcount,2)



    @classmethod
    def tearDownClass(cls):
        BROWSER.quit()
