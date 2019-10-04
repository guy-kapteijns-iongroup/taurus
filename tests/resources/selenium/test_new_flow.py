# coding=utf-8

import logging
import random
import string
import sys
import unittest
from time import time, sleep

import apiritif

import os
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, NoSuchFrameException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as econd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

from bzt.resources.selenium_extras import FrameManager, WindowManager


def setup():
    # todo: avoid duplicate setup calls
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service_log_path='webdriver.log',
                              chrome_options=options)
    driver.implicitly_wait(60.0)
    func_mode = False       # don't stop after failed test case
    flow_markers = True     # send flow markers to webdriver
    vars = {

    }
    apiritif.put_into_thread_store(vars=vars, driver=driver, func_mode=func_mode, flow_markers=flow_markers)


def teardown():
    driver = apiritif.get_from_thread_store("driver")
    driver.quit()


class TestSdsdsdsSelenium(unittest.TestCase):

    def setUp(self):
        self.vars, self.driver = apiritif.get_from_thread_store(("vars", "driver"))
        self.wnd_mng = WindowManager(self.driver)
        self.frm_mng = FrameManager(self.driver)

    def test_them_all(self):
        with apiritif.smart_transaction(name='t1'):
            self.driver.get('http://blazedemo.com/purchase.php')
            self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

        with apiritif.smart_transaction(name='t2'):
            self.driver.get('https://www.belarus.by/en/')
            body = self.driver.page_source
            re_pattern = re.compile('In God we trust')
            self.assertNotEqual(0, len(re.findall(re_pattern, body)), "Assertion: 'In God we trust' not found in BODY")

        with apiritif.smart_transaction(name='t3'):
            self.driver.get('some.strange.url')