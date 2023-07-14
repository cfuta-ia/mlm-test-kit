from .task import Task
from selenium.webdriver.common.action_chains import ActionChains


class TestSequence:
    """ """
    def __init__(self, name, url, actions=[]):
        self.name = name
        self.url = url
        self.actions = [Task(**task) for task in actions]

    def assess(self, driver):
        """ """
        driver.get(self.url)
        for task in self.actions:
            task.assess(driver)
            print(task)

    def __repr__(self) -> str:
        return f'Page URL -- {self.url}'