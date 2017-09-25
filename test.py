import unittest
import urllib3
from flask import Flask
from flask_testing import TestCase, LiveServerTestCase
from selenium import webdriver
from app import create_app

class myTest(LiveServerTestCase):

    #test variables
    test_str1 = "stuff"
    test_str2 = "junks"
    test_metrics = "levenshtein"

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['LIVESERVER_PORT'] = 8943
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.get_server_url())
        #self.baseURL = "http://localhost:5000/calculator"

    def test_calc(self):
        self.driver.find_element_by_id("string1").send_keys(test_str1)
        self.driver.find_element_by_id("string2").send_keys(test_str2)
        self.driver.find_element_by_id("choose_method").send_keys(test_metrics)
        self.driver.find_element_by_id("button").click()
        self.assertEqual(self.driver.find_element_id("result"), 5)
        

    def test_main_page(self):
        http = urllib3.PoolManager()
        response = http.request('GET', self.get_server_url())
        self.assertEqual(response.status, 200)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()   
    

