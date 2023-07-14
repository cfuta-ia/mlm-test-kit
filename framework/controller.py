from .util import webdriver, configuration
from .util.test_sequence import TestSequence

class Controller:
    """ """
    def __init__(self):
        for key, value in configuration.get().items():
            setattr(self, key, value)
        self.tests = [TestSequence(**sequence) for sequence in self.tests]

    def assess(self):
        """ """
        print(f'Name: {self.name}')
        ## Do the things 
        driver = webdriver.get()
        #driver = None
        for sequence in self.tests:
            print(f'\n{sequence}')
            sequence.assess(driver)
        
        if self.closeOnComplete:
            driver.quit()
