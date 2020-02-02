from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen as uReq
import wget
import requests as req
import os
import random
import time
from progress.bar import (Bar)
"""
import time
import progressbar
import logging
"""
url = "https://www.google.com/"
uClient = uReq(url)
html_page = uClient.read()
uClient.close()

page_soup =soup(html_page,"html.parser")

#print(page_soup.findAll("html"))

containers = page_soup.findAll("a", href=True)
num = len(containers)
for link in range(0,num):
	#linki =str(link)
	print(str(link +1) + '. ' + str(containers[link]['href']))

	
print()
print("Downloading starting soon...............:")
print()
number1 = 10
#wget.download(url, 'c:/pyth/dwnlds/pythonLogo_' + str(number1) + '.txt')

def sleep():
    t = 0.01
    t += t * random.uniform(-0.1, 0.1)  # Add some variance
    time.sleep(t)


for link in range(0,3):
	#wget.download(containers[link]['href'], 'c:/pyth/webscriping/dwnlds/test_' + str(link + 1) + '.txt')
	#resp = req.get(containers[link]['href'])

	file_name = 'c:/pyth/webscriping/dwnlds/Paper__' + str(link + 1) + '.txt'
	file_stats = os.stat(file_name)
	print('  Downloading page content for  Link ' + str(link + 1) + ' ' + str(file_stats.st_size) + ' Bytes received  Status: Progressing')

	#wget.download(containers[link]['href'], 'c:/pyth/webscriping/dwnlds/Paper__' + str(link + 1) + '.txt')
	#print('  Downloading page content for  Link ' + str(link + 1) + ' ' + str(file_stats.st_size) + ' Bytes received  Status: Progressing')
	#print('  Downloading page content for  Link ' + str(link + 1) + '...')

print()
print("Downloading starting...............:")
print()
suffix = '%(index)d/%(max)d [%(elapsed)d / %(eta)d / %(eta_td)s]'
bar =Bar(Bar.__name__,suffix=suffix)
for link in range(0,3):
	#wget.download(containers[link]['href'], 'c:/pyth/webscriping/dwnlds/test_' + str(link + 1) + '.txt')
	#resp = req.get(containers[link]['href'])

	file_name = 'c:/pyth/webscriping/progress-1.5/dwnlds/Paper__' + str(link + 1) + '.txt'
	file_stats = os.stat(file_name)
	
	wget.download(containers[link]['href'], 'c:/pyth/webscriping/progress-1.5/dwnlds/PaperTest__' + str(link + 1) + '.txt')
	print('  Downloading page content for  Link ' + str(link + 1) + ' ' + str(file_stats.st_size) + ' Bytes received  Status: Progressing')




