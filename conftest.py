import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    print("\nstart browser for test..")
    # Выбор языка
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # Создать элемент с заданными опциями
    browser = webdriver.Chrome(options=options)
    
    yield browser
    # Перед закрытием оставить страницу на 2 секунды для визуального контроля
    time.sleep(2)
    print("\nquit browser..")
    browser.quit()
