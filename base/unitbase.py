import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from common.util import projjectpath, configAdress


class unitbase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # path = Service(projectpath()+"dr\\chromedriver.exe")
        path = Service(projjectpath() + "driver\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=path)
        cls.driver.get(configAdress("testUrl", "url"))

    def tearDownClass(cls):
        cls.driver.quit()
        print("test over")
