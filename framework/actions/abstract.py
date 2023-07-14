from abc import ABC, abstractmethod
class AbstractAction(ABC):
    """ """
    pause = 5
    @abstractmethod
    def addAction(self):
        """ """
        pass
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}'