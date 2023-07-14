from .abstract import AbstractAction
def addToChain(chain, action, **kwargs):
    """ """
    obj = globals().get(action)
    if obj == None:
        raise ValueError("Invalid Action")
    else:
        obj.addAction(chain, **kwargs)
    return None

class Click(AbstractAction):
    """ """
    @classmethod
    def addAction(cls, chain, *element):
        """ """
        chain.click(element)
        chain.pause(cls.pause)