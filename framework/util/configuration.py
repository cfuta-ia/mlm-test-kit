import os, json

def get():
    """ """
    return Configuration()

class Configuration:
    """ """
    def __init__(self):
        self.__dict__.update(self.jsonFile())

    @staticmethod
    def jsonFile():
        with open(os.path.join(os.getcwd(), 'framework', 'test.json'), 'r') as f:
            data = json.load(f)
        return data