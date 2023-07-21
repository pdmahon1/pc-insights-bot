"""
    A Singleton class that stores the data from the Newmaxx spreadsheet.
"""

class SsdDataService(object):    
    _data = None
    _timestamp = None
    _instance = None

    def __init__(self):
        _data = None
        _timestamp = None
        _instance = self

    def __new__(cls):
        if cls._data == None:
            super(SsdDataService, cls).__init__(cls)
        return cls._instance
    
    @staticmethod
    def instanceof(self):
        return SsdDataService()

    def _is_data_current(self):
        '''
        1 get latest timestamp
        2 return True if timestamps match
        '''
        pass

    def _update(self):
        # if data is current, don't update
        # else, update the data
        pass
    