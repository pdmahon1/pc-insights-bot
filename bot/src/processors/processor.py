from abc import ABC, abstractmethod


class Processor(ABC):
    def __init__(self):
        raise Exception("The Processor class is an interface. " + 
                        "Instantiate a class that inherits Processor")
    
    @abstractmethod 
    def extract_data_from_title(self, title: str) -> dict:
        pass