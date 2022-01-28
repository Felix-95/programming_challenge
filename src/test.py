import os
from constants import PROJECT_DIR


def test_read_write():
    """reads data from xml, writes it to new one any compares the initial data with the newly written.
    if the match read and write functions work properly
    """
    from write_xml import write_to_xml
    from read_xml import read_from_xml

    original_data = read_from_xml("tests", "test")

    new_file_name = "new_data"
    write_to_xml(original_data, "tests", file_name = new_file_name)

    reread_data = read_from_xml("tests", new_file_name)

    os.remove(PROJECT_DIR + "/tests/" + new_file_name + ".xml") 
    assert reread_data == original_data
    print("[TEST]: read_write test successfull")

def test_initialize_browser():
    """checks type of created browser 

    Returns:
        [Webdriver]: Firefox browser
    """
    from helper import initialize_browser
    browser = initialize_browser()
    
    assert str(type(browser)) == "<class 'selenium.webdriver.firefox.webdriver.WebDriver'>"
    print("[TEST]: initialize_browser test successfull")
    return browser

def test_search_product(browser):
    """searches product and compares it to successfully scraped data

    Args:
        browser ([Webdriver]): Firefox browser
    """
    from scraper import search_product
    from read_xml import read_from_xml
    
    setpoint = read_from_xml("tests", "example_product")[0]
    
    test_marke =  "Stylecraft"
    test_bezeichung = "Bambino DK"
    
    product = search_product(browser, test_marke, test_bezeichung)
    
    # convert bool to str to be comparable to setpoint
    try:
        product["Lieferbar"] = str(product["Lieferbar"])
    except:
        pass
   
    assert setpoint == product
    print("[TEST]: search_product test successfull")
    
    
test_read_write()
browser = test_initialize_browser()
test_search_product(browser)
browser.close()
