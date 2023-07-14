class Locator:
    """ """
    def __init__(self, key, identifier):
        self.key = key
        self.identifier = identifier

    @property
    def element(self):
        """ """
        return (self.key, self.identifier)
    
    def __iter__(self):
        return iter(self.element)
        