'''
sheet_delegator.py

Interacts with the Newmaxx Google Sheet.
'''
from src.main.delegators import delegator as Delegator

class SsdDelegator:
    def __init__(self):
        ssd_data = self.SsdData()
        pass




    class SsdData(object):
        """
        A Singleton class that stores the data from the Newmaxx spreadsheet
        """
        _data = None
        _timestamp = None

        def __init__(self):
            # TODO initialize the data and timestamp
            pass

        def __new__(cls):
            if cls._data == None:
                super(SsdData, cls).__init__(cls)
            return cls._data
        



