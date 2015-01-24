#!/usr/bin/python
# my CTA bus tracker
# ray@truedays 01/15/2015
import sys
import requests
from bs4 import BeautifulSoup

#print sys.argv

if len(sys.argv) < 2:
 print "Please provide at least one URL!"

# get all arguments:
for list in sys.argv[1:]:
# print list
 # validate URL here
# r = requests.get(list)
 r = requests.get(list)
# print r.status_code
 soup = BeautifulSoup(r.text)
 links = soup.find_all('a')
 linkCount = str(len(links))

 print " ----- " + linkCount + " links extracted ----- "
 #print soup.find_all('a')
 for link in links:
  print link.get('href')



