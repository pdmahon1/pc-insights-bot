

from src.main.models.model import Model
from src.main.processors.processor import Processor


class SsdProcessor(Processor):
    def __init__(self):
        pass


    @staticmethod
    def extract_data_from_title(self, title: str) -> Model:
        # Using the title, parse the SSD information to retrieve device info
        # and to create and return a SsdModel
        
        pass