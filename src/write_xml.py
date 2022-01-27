import xml.etree.ElementTree as ET
import datetime
from constants import PROJECT_DIR

def write_to_xml(lst):
    """parses list of dictionaries and creates xml file with each dicts key-value pairs being elements

    Args:
        lst ([list]): list of dicts
        
    Returns:
        [str]: path to the newly created xml file
    """
    # files can be sorted by time of title
    file_name = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    output_path = PROJECT_DIR + "/output/" + file_name + ".xml"

    root = ET.Element('root')
    for dictionary in lst:
        product = ET.SubElement(root, "product")
        for key, value in dictionary.items():
            trait = ET.SubElement(product, key)
            trait.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(output_path,encoding="UTF-8",xml_declaration=True)
    
    return output_path
    