import xml.etree.ElementTree as ET
import datetime
from constants import PROJECT_DIR

def read_from_xml(folder, file_name):
    """parses list of dictionaries and creates xml file with each dicts key-value pairs being elements

    Args:
        lst ([list]): list of dicts
        
    Returns:
        [str]: path to the newly created xml file
    """
    # files can be sorted by time of title
    xml_path = PROJECT_DIR +"/" + folder + "/" + file_name + ".xml"

    tree = ET.parse(xml_path)
    root = tree.getroot()
    products_lst = []
    for product in root:
        product_dict = {}
        for trait in product:
            product_dict[trait.tag] = trait.text
            
        products_lst.append(product_dict)
    
    
    return products_lst
    # 2022-01-27--20-13-24