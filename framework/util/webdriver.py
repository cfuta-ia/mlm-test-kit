from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def get():
    """ """
    return Firefox(service=Service(GeckoDriverManager().install()), options=FirefoxOptions())