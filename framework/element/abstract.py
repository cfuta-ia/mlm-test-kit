from abc import ABC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
    
class AbstractElement(ABC):
    """ """
    PAUSE = 1
    WAIT = 1
    FORMAT_STRING = "{}"
    def __init__(self, value='', key='id', formatValue=True):
        self.locateBy = self.getLocatorBy(key)
        self.locateValue = self.getLocateValue(value, formatValue)

    @classmethod
    def getLocatorBy(cls, key):
        """ """
        match key:
            case 'id':
                value = By.ID
            case 'class':
                value = By.CLASS_NAME
            case 'xpath':
                value = By.XPATH
            case other:
                value = None
        return value
    
    @classmethod
    def getLocateValue(cls, value, formatValue):
        """ """
        return cls.FORMAT_STRING.format(value.lower()) if formatValue else value
    
    def getLocator(self):
        """ """
        return (self.locateBy, self.locateValue)
    
    def getElement(self, driver):
        """ """ 
        element = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(*self.getLocator()))
        return element
    
    def log(self, action):
        """ """
        print(f'{self.__class__.__qualname__} ({self.locateValue}) - {action}')
        return None
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}'