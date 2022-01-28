
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from constants import URL

def get_product_properties(browser):
    
    properties = {}
    search_result = browser.find_element(By.CLASS_NAME, "sooqrSearchResults")
    
    title = search_result.find_element(By.CLASS_NAME, "productlist-title")
    title.find_element(By.TAG_NAME, "a").click()
    
    time.sleep(0.1)
    
    content_place_holder = browser.find_element(By.ID, "pdetailTableSpecs")
    table_body = content_place_holder.find_element(By.TAG_NAME, "tbody")
    
    useful_keys = ["Zusammenstellung", "Nadelstärke"]
    for table_row in table_body.find_elements(By.TAG_NAME, "tr"):
        key, value = table_row.find_elements(By.TAG_NAME, "td")
        if key.text in useful_keys:
            properties[key.text] = value.text
    
    try:
        properties["Lieferbar"] = True if browser.find_element(By.CLASS_NAME, "stock-green").text == "Lieferbar" else False 
    except:
        properties["Lieferbar"] = False
        
    properties["Preis"] = browser.find_element(By.CLASS_NAME, "product-price-amount").text
            
    return properties

def select_correct_brand(browser, marke):
    """checks if any search results were found and if they are from the correct marke

    Args:
        browser ([webdriver]): Firefox browser
        marke ([str]): 

    Returns:
        [str]: returns error message if the correct prodcut can not be found
    """

    # try to locate marken_filter
    try:
        marken_search_filter = browser.find_element(By.ID, "sooqr44898be26662b0dfSearchFilter191640")
        marken_search_filter_field = marken_search_filter.find_elements(By.TAG_NAME, "input")
    except NoSuchElementException:
        return "No search result found"
    
    # try to click marke
    for marken_input in marken_search_filter_field:
        test_marke = marken_input.get_attribute("value")
        if test_marke == marke:
            marken_input.click()
            break
    else:
        return "No such brand for search term"
    return ""

def search_product(browser, marke, bezeichnung):
    """webscrapes all needed information for product
    
    Args:
        browser ([webdriver]): Firefox browser
        marke ([str]): 
        bezeichnung ([str]): 

    Returns:
        [dict]: dictionary of properties of searched products
    """
    
    # nativating to url (home) of site everytime before searching for product becuase occationally elements could not 
    # be found (although visible) after continuing from previous product site
    browser.get(URL)
    
    search_field = browser.find_element(By.ID, "searchSooqrTop")
    search_field.clear()
    search_field.send_keys(bezeichnung)
    
    product_properties = {"marke": marke, "bezeichnung": bezeichnung}

    # checking for errors like not finding any element when searching for bezeichnung or none of the correct marke
    occured_errors = select_correct_brand(browser, marke)
    if occured_errors != "":
        product_properties["error"] = occured_errors
        return product_properties
    
    product_properties.update(get_product_properties(browser))

    return product_properties