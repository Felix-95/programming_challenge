from constants import PROJECT_DIR, URL
from scraper import search_product
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import xlrd

def initialize_browser(headless_browser=False):
    """initializes Firefox browser and returns it

    Args:
        headless_browser (bool, optional): When True Browserwindow is not visible. Defaults to False.

    Returns:
        [webdriver]: Firefox browser
    """
    browser_options = Options()
    if headless_browser:
        browser_options.headless = True

    browser_path = PROJECT_DIR + "/browser/geckodriver.exe"
    browser = Firefox(executable_path=browser_path, options=browser_options)
    browser.implicitly_wait(4)
    
    browser.get(URL)
    try_acceping_cookies(browser)
    
    return browser

def get_products():
    """reads marke and bezeichnung from products table

    Returns:
        [list]: (marke, bezeichnung) tuple pairs
    """
    products_path = PROJECT_DIR + "/data/products.xls"
    xls_sheet = xlrd.open_workbook(products_path).sheet_by_index(0)
    
    products = [(xls_sheet.cell_value(x , 0), xls_sheet.cell_value(x, 1)) for x in range(xls_sheet.nrows)]
        
    return products

def try_acceping_cookies(browser):
    """tries accepting cookies

    Args:
        browser ([webdriver]): Firefox browser
    """
    try:
        accept_button = browser.find_element(By.ID, "AcceptReload")
        accept_button.click()
    except:
        print("Could not accept cookies because didn't find the element")