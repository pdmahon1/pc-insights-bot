#an interface
from abc import ABC, abstractmethod


class Model(ABC):
    def __init__(self):
        raise Exception("The Model class is an interface. " + 
                        "Instantiate a class that inherits Model")
    
    @abstractmethod
    def get(self, category:str) -> str:
        pass
