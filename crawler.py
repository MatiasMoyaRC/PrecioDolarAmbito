# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


class Crawler:

    def __init__(self, head):
        self.head = head

    def create_driver(self):

        options = Options()
        options.headless = self.head
        driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
        driver.maximize_window()

        return driver

    def crawl(self, drive, url):
        drive.get(url)
        time.sleep(5)
