'''
Interacts with CamelCamelCamel website
'''

class CamelCamelCamel:

    def __init__(self):
        BASE_URL = "https://camelcamelcamel.com/search?sq="

    def __convert_query_for_url(self, query:str) -> str:
        return "+".join(query.split(' '))
    
    def get_url_from_query(self, query:str) -> str:
        return self.BASE_URL + self.__convert_query_for_url(query)


