import src.main.delegators


class DelegatorFactory:
    _instance = None

    def __init__(self):
        self._delegators = {}

    def __new__(self, cls):
        if cls._instance == None:
            cls._instance = super(DelegatorFactory, cls).__new__(cls)
        return cls._instance
    
    def get(self, type:str) -> Processor:
        return self._processors[type] if type in self._processors else None
    
    @staticmethod
    def can_process(self, type:str) -> bool:
        return False if type == None else type.lower() in self._processors