#! encoding: utf-8
"""
电影天堂，电影磁力链
"""
import requests
from bs4 import BeautifulSoup
from lxml import etree
import time
import random

with open('data.txt') as f:
    row = f.read()
    row = eval(row)
    for i in row:
        if len(i) > 2:
            print(i)
            with open('data_clean.txt', 'a') as wf:
                wf.write(str(i))
