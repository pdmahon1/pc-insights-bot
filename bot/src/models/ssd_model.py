from src.main.models.model import Model

class SsdModel(Model):
    '''
    A wrapper class for a map whose keys are the attributes associated with 
    the NewMaxx spreadsheet. The keys directly correspond to information about
    SSD's.
    '''
    def __init__():
        _specs = {}
        _specs["brand"] = ""
        _specs["model"] = ""
        _specs["interface"] = ""
        _specs["form_factor"] = ""
        _specs["capacities"] = ""
        _specs["controller"] = ""
        _specs["configuration"] = ""
        _specs["dram"] = ""
        _specs["hmb"] = ""
        _specs["nand_brand"] = ""
        _specs["nand_type"] = ""
        _specs["layers"] = ""
        _specs["rw_speed"] = ""
        _specs["categories"] = ""
        _specs["brand"] = ""

    def get(self, category:str):
        return self._specs[category] if category in self._specs else ""
