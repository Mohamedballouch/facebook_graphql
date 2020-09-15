# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:31:59 2020

@author: BALLOUCH

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.firefox.options import Options
import sys
import time
import calendar
from bs4 import BeautifulSoup as bs
import json
import re
import requests
import datefinder
import re
import lxml

id_post=10158642076581655

URL = f'https://www.facebook.com/pg/Hespress/posts/{id_post}'

page = requests.get(URL).text


html_soup = bs(page,'lxml')


ty=html_soup.prettify()

tx1=re.compile("feedbackTargetID")

link=html_soup.find("script",text=tx1)

text4 = re.sub("<[^>]*>","",str(link))


feedback_id=text4.partition('"feedbackTargetID":"')[2].partition('","focusCommentID"')[0]



link1=html_soup.find('link',{"as":"script"})
extract_link=link1['href']

resp=requests.get(extract_link)

string_t=str(resp.text)

doc_id=string_t.partition('"UFI2CommentsProviderPaginationQuery",operationKind:"query"')[0]
doc_id=doc_id.partition('"UFI2CommentsProviderPaginationQuery"')[2]
doc_id=doc_id.partition('"UFI2CommentsProviderPaginationQuery"')[2]
doc_id=doc_id.partition('params:{id:"')[2]
doc_id=doc_id.partition('",metadata')[0]











