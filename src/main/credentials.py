from os.path import exists
import json

class Credentials:
    @staticmethod
    def get_credentials_from_json(self, filename: str):
        """
        If the given file exists, return a dictionary of the contents
        If file doesn't exist or the existing file is not JSON formatted,
        then return an empty dictionary

        Parameters:
        filename - the location of the JSON file. It may be relative to this 
            class file or an absolute file location
        """
             
        try:
            if not exists(filename):
                raise FileNotFoundError()
            with open(filename, "r") as json_file:
                return json.load(json_file)
        except Exception as error:
            print("ERROR raised! Type '{}'".format(type(error)))
            return dict()
        finally:
            json_file.close()
