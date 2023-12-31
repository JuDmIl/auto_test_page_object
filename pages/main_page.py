# импорт базового класса BasePage
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

# Класс MainPage - наследник класса BasePage
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click() 
    # метод, который будет проверять наличие ссылки
    def should_be_login_link(self):
        #self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
