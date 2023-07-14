from abc import ABC, abstractproperty
class AbstractLocator(ABC):
    """ """
    @abstractproperty
    def key(self):
        """ """
        pass

    @abstractproperty
    def locator(self):
        """ """
        pass

    @classmethod
    def elementDefinition(cls):
        """ """
        return (cls.key, cls.identifier)
    
    @classmethod
    def getElement(cls, driver):
        """ """ 
        return driver.find_element(*cls.elementDefinition())
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}'