from abc import ABC, abstractproperty
from selenium.webdriver.common.by import By
    
class AbstractLocator:
    """ """
    FORMAT_STRING = "{}"
    def __init__(self, value, key='id'):
        self.locateBy = self.getLocatorKey(key)
        self.locateValue = self.getLocateValue(value)

    @classmethod
    def getLocatorBy(cls, key):
        """ """
        match key:
            case 'id':
                value = By.ID
            case other:
                value = None
        return value
    
    @classmethod
    def getLocateValue(cls, value):
        """ """
        return cls.FORMAT_STRING.format(value.lower())
    
    def getLocator(self):
        """ """
        return (self.locateBy, self.lovateValue)
    
    def getElement(self, driver):
        """ """ 
        return driver.find_element(*self.getLocator())

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}'