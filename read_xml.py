from lxml import etree as r

TAGS = ["browser_type", "excepted_title", "first_name", "mail", "password", "password_confirm"]

class ReadConfig:

    def __init__(self, file_name):
        self.__tree = r.parse(file_name).getroot()

    def get_text(self, tag_name):
        return self.__tree.find(tag_name).text
