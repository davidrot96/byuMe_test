from lxml import etree as r


class CreateConfig:

    def __init__(self, root_name):
        self.__root = r.Element(root_name)
        self.__tree = r.ElementTree(self.__root)

    def add_child(self, tag_name, text):
        r.SubElement(self.__root, tag_name).text = text

    def write_to_file(self, file_name):
        print(file_name)
        self.__tree.write(file_name, pretty_print=True, xml_declaration=True, encoding='utf-8')