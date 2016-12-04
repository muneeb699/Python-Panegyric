# -*- coding: utf-8 -*-
"""
Created on Sun Dec 04 23:16:48 2016

@author: Muneeb ul Hassan
"""

import requests
from bs4 import BeautifulSoup
url = "https://www.yelp.com.au/search?find_desc=Restaurants&find_loc=Melbourne+Victoria&ns=1"
yelp = requests.get(url)
yelp_soup = BeautifulSoup(yelp.text,'html.parser')
yelp_soup.prettify()
for link in yelp_soup.findAll('a'):
    print(link)