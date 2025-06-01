from src.main.processors.processor import Processor
from src.main.processors.ssd_processor import SsdProcessor


class ProcessorFactory:
    def __init__(self):
        self._processors = {
            "ssd": SsdProcessor()
        }

    def get(self, type:str) -> Processor:
        return self._processors[type] if type in self._processors else None
    
    def can_process(self, type:str) -> bool:
        return False if type == None else type.lower() in self._processors