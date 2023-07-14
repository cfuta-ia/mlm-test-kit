from .abstract import AbstractLocator
from selenium.webdriver.common.by import By
from pydoc import locate

def get(name, **kwargs):
    """ """
    locator = globals().get(name)
    if locator != None:
        return locator(**kwargs)
    else:
        raise ValueError(f"Locator '{name}' does not exist.")
    return globals().get(locator)

class Button(AbstractLocator):
    """ """
    FORMAT_STRING = "{}-button"

class TextField(AbstractLocator):
    """ """
    FORMAT_STRING = "{}-field"