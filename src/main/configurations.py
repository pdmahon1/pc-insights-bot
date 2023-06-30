from os.path import exists
import json

class Configurations:
    @staticmethod
    def get_configs_from_json_file(self, filename: str) -> dict:
        """
        If the given file exists, return a dictionary of the contents
        If file doesn't exist or the existing file is not JSON formatted,
        then return an empty dictionary

        Parameters:
        filename - the location of the JSON file. It may be relative to this 
            class file or an absolute file location
        """
    
        if not exists(filename):
            raise FileNotFoundError("File '{}' not found".format(filename))

        with open(filename, "r") as json_file:
            return json.load(json_file)
