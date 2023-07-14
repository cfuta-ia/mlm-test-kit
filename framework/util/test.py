from ..element import element

class Test:
    """ """
    def __init__(self, name, url, steps):
        self.name = name
        self.url = url
        self.steps = steps
        self.elements = {}

    def setElement(self, key, value):
        """ """
        self.element[key] = value

    def getElement(self, key):
        """ """
        return self.element[key]
    
    def hashElement(self, **kwargs):
        """ """
        hashKey = hash(kwargs.items())
        if hashKey in self.elements.keys():
            obj = self.getElement(hashKey)
        else:
            obj = element.get(**kwargs)
            self.setElement(hashKey, obj)
        return obj
    
    def evaluate(self, driver):
        """ """
        self.logName()
        driver.get(self.url)
        driver.implicitly_wait(2)
        for step in self.steps:
            obj = self.hashElement(**step['element'])
            obj.action(driver)
        self.logName()

    def logName(self):
        """ """
        print(f'----{self.name}----')


    @staticmethod
    def fromObject(obj):
        """ """
        return Test(**obj)
