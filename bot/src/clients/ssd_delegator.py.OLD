'''
sheet_delegator.py

Interacts with the Newmaxx Google Sheet.
'''

from datetime import time


class SsdDelegator:
    _instance = None

    def __init__(self):
        self._username = ""
        self._password = ""
        self._ssd_data = None
        self._spreadsheet_last_updated = None
        self._spreadsheet_url = ""


    def __new__(cls, configs):
        if cls._instance == None:
            cls._instance = super(SsdDelegator, cls).__new__(cls)
            
            cls._spreadsheet_url = configs["url"]
            cls._spreadsheet_last_updated = None #TODO get this from the google sheet
        


    def update(self):
        # get new data
        # compare data and replace self._ssd_data if there's newer
        #     -> then update self._spreadsheet_last_updated
        pass

    def last_updated(self):
        return self._last_update



