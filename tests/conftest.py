import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from config.config import TestData
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')
    options.add_argument('--start-fullscreen')
    options.add_argument('--new-window')
    return options


@pytest.fixture
def get_chrome_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    return driver


"""If some problems with installing chromedriver arise, this method with installing chromedriver from
the project directory may be used instead"""
# @pytest.fixture
# def get_chrome_webdriver(get_chrome_options):
#     options = get_chrome_options
#     # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#     driver = webdriver.Chrome('config/chromedriver', options=options)
#     return driver


@pytest.fixture()
def setup(request, get_chrome_webdriver):
    driver = get_chrome_webdriver
    url = TestData.BASE_URL
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.close()
    # driver.quit()
