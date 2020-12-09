from selenium import webdriver
import time
from selenium.webdriver import chrome
from selenium.webdriver import firefox


class Crawler:

    def __init__(self, browser, head):
        self.browser = browser.lower()
        self.head = head

    def create_driver(self):
        # options = Options()
        # options.headless = self.head

        if self.browser == "chrome":
            options = chrome.options.Options()
            options.headless = self.head
            driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
        else:
            driver = webdriver.Firefox(executable_path="geckodriver.exe")
        driver.maximize_window()

        return driver

    def crawl(self, drive, url):
        drive.get(url)
        time.sleep(5)
