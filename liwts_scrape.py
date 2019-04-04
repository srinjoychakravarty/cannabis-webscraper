import requests
from bs4 import BeautifulSoup

strains_url = 'https://www.liwts.org/strain-reviews/indica-strains/page/'
page_num = 4
hyperlink = strains_url + str(page_num)
current_page = requests.get(hyperlink)
http_okay = current_page.status_code
if (http_okay == 200):
    print(current_page .content)
