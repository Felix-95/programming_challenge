import datetime
start = datetime.datetime.now()
from helper import initialize_browser, get_products
from scraper import search_product
from write_xml import write_to_xml
from constants import URL


products = get_products()
browser = initialize_browser()
  
product_properties_lst = []
for marke, bezeichnung in products:
    product_properties_lst.append(search_product(browser, marke, bezeichnung))
    
browser.close()
file_path = write_to_xml(product_properties_lst)

end = datetime.datetime.now()
delta = end - start
print("created xml file stored at {file_path}")
print(f"scraping finished in {delta}")