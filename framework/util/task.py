from .locator import Locator
from selenium.webdriver.support.ui import WebDriverWait

class Task:
    """ """
    def __init__(self, name, identifier, key='id', action='click'):
        self.locator = Locator(key, identifier)
        self.name = name
        self.action = action
        self.result = None

    def action(self, driver):
        """ """
        driver.find_element(*self.locator).click()
        return None
    
    def assess(self, driver):
        """ """
        try:
            WebDriverWait(driver, 30).until(lambda driver: driver.find_element(*self.locator))
            self.action()
            self.result = 'pass'
        except Exception as e:
            self.result = str(e)
        
    def __repr__(self) -> str:
        return f'Task -- {self.name}\n  Action: {self.action}\n  Result: {self.result}'