import xml.etree.ElementTree as ET
import datetime
from constants import PROJECT_DIR

def write_to_xml(lst, folder, file_name = None):
    """parses list of dictionaries and creates xml file with each dicts key-value pairs being elements

    Args:
        lst ([list]): list of dicts
        folder ([str]): folder relativ from base folder
        file_name ([str], optional): If file_name is provided it overrides the time format. Defaults to None.

    Returns:
        [str]: path to the newly created xml file
    """
    # files can be sorted by time of title
    if not file_name:
        file_name = "wollplatz" + "--" + datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
    output_path = PROJECT_DIR + "/" + folder + "/" + file_name + ".xml"

    root = ET.Element('root')
    for dictionary in lst:
        product = ET.SubElement(root, "product")
        for key, value in dictionary.items():
            trait = ET.SubElement(product, key)
            trait.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(output_path,encoding="UTF-8",xml_declaration=True)
    
    return output_path
    