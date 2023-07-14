from uuid import uuid4
from .abstract import AbstractElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def get(name, **kwargs):
    """ """
    element = globals().get(name)
    if element != None:
        return element(**kwargs)
    else:
        raise ValueError(f"Element '{name}' does not exist.")
    
class Button(AbstractElement):
    """ """
    FORMAT_STRING = "{}-button"
    def click(self, driver):
        """ """
        ActionChains(driver).move_to_element(self.getElement(driver)).click().pause(self.PAUSE).perform()
        driver.implicitly_wait(self.WAIT)
        self.log('Click')
        return None

class TextField(AbstractElement):
    """ """
    FORMAT_STRING = "{}-field"
    def fillText(self, driver, text=None):
        """ """
        text = str(text if text != None else uuid4())
        ActionChains(driver).move_to_element(self.getElement(driver)).click().send_keys(text).send_keys(Keys.TAB).pause(self.PAUSE).perform()
        driver.implicitly_wait(self.WAIT)
        self.log('Fill Text')
        return None

class Option(AbstractElement):
    """ """
    FORMAT_STRING = "{}-option"
    def click(self, driver):
        """ """
        ActionChains(driver).move_to_element(self.getElement(driver)).click().pause(self.PAUSE).perform()
        driver.implicitly_wait(self.WAIT)
        self.log('Click')
        return None

class FileUpload(AbstractElement):
    """ """
    def __init__(self):
        AbstractElement.__init__(self, value="//*[@id='file-upload']/div[2]/div[1]/input", key="xpath")

    def upload(self, driver, path):
        self.getElement(driver).send_keys(path)
        driver.implicitly_wait(self.WAIT)
        self.log('Upload')
        return None