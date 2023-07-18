from framework.util import webdriver
from framework.util.configuration import Configuration
from framework.util.test import Test


class Controller(Configuration):
    """ """
    def __init__(self):
        Configuration.__init__(self)

    def evaluate(self):
        """ """
        print(f'Starting Test\n{self.name}\n')
        driver = webdriver.get()
        for obj in self.tests:
            test = Test.fromObject(obj)
            test.evaluate(driver)
            print('')

        if self.closeOnComplete:
            driver.quit()
        print('Ending Test')
