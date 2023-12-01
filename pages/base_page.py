from selenium.common.exceptions import NoSuchElementException # перехват исключения
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # команда неявного ожидания 10 с
        self.browser.implicitly_wait(timeout)
    def open(self):
        self.browser.get(self.url)
    # метод для перехватывания исключений
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

        
