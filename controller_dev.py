from framework.util import webdriver
from framework.util.configuration import Configuration
from framework.util.test import Test


class Controller(Configuration):
    """ """
    def __init__(self):
        Configuration.__init__(self)

    def evaluate(self):
        """ """
        print(f'Starting Test\n{self.name}')
        driver = webdriver.get()
        for t in self.tests:
            test = Test.fromObject(**t)
            test.evaluate(driver)

        if self.closeOnComplete:
            driver.quit()
        print('Ending Test')

controller = Controller().evaluate()
