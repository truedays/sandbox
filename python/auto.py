#!/usr/bin/python
# -*- coding: UTF-8 -*-
# CTA API CLI YAH

import sys
import requests
#from bs4 import BeautifulSoup
from xmltodict import parse
import datetime
from time import gmtime, strftime
# enable debugging
import cgitb
cgitb.enable()

# get API key from file
f = open('./.cta-api.key', 'r')
APIKEY = "?key=" + f.read(25)
f.close()

URL="http://www.ctabustracker.com/bustime/api/v1/"
apicmd =  "getpredictions"

showResponse = ["stpnm","stpid","vid","rt","rtdir","prdtm"]

def getPred(localurl):
 r = requests.get(localurl)
 out = parse(r.text)
 if "error" in out['bustime-response']:
  #print "+" + str(out) + "+"
  #print "localurl: " + str(localurl)
  print "xXxXxXx\nERROR: " + out['bustime-response']['error']['msg']
  print "xXxXxXx\n"
  #sys.exit(1)
  return
 print "___"
 # Lame safety check:
 if "prdtm" in out['bustime-response']['prd']:
  #print "tmpstmp: " + out['bustime-response']['prd']['tmstmp']
  for x in showResponse:
   print x + ": " + out['bustime-response']['prd'][x] 
   #out['bustime-response']['prd']:
   #print key
   #print x
 
 # true == multiple predictions returned
 if isinstance(out['bustime-response']['prd'], list):
  for x in range(0,len(out['bustime-response']['prd'])):
   if out['bustime-response']['prd'][x]:
    hourNow=int(out['bustime-response']['prd'][x]['tmstmp'][9:11])
    minNow=int(out['bustime-response']['prd'][x]['tmstmp'][12:14])
    hourPred=int(out['bustime-response']['prd'][x]['prdtm'][9:11])
    minPred=int(out['bustime-response']['prd'][x]['prdtm'][12:14])
    timeRemain = ((hourPred*60)+minPred) - ((hourNow*60)+minNow)
    for response in showResponse:
     print response + "[" + str(x) + "]" + ": " + out['bustime-response']['prd'][x][response]
    print "Minutes remaining: " + str(timeRemain)
    print "___"
 else:
  if "tmstmp" in out['bustime-response']['prd']:
   # print out['bustime-response']['prd']['tmstmp'][9:11]
   # print out['bustime-response']['prd']['tmstmp'][12:14]
   # print out['bustime-response']['prd']['prdtm'][9:11] 
   # print out['bustime-response']['prd']['prdtm'][12:14]
   hourNow=int(out['bustime-response']['prd']['tmstmp'][9:11])
   minNow=int(out['bustime-response']['prd']['tmstmp'][12:14])
   hourPred=int(out['bustime-response']['prd']['prdtm'][9:11])
   minPred=int(out['bustime-response']['prd']['prdtm'][12:14])
   timeRemain = ((hourPred*60)+minPred) - ((hourNow*60)+minNow)
   print "Minutes remaining: " + str(timeRemain)
   print "___"

if int(strftime("%H", gmtime())) > 18 or int(strftime("%H", gmtime())) < 6 :
 # Heading home
 heading = "home"
 stops = ["&rt=78&stpid=11401", "&rt=56&stpid=14101"]
else:
 # heading to work
 heading = "work"
 stops = ["&rt=78&stpid=11321", "&rt=56&stpid=5586"]

#print "Content-Type: text/plain;charset=utf-8"
print
print "<html><title>Bus times - Heading to " + heading + "</title><body>"
print "<pre>"
print "hour: " + str(int(strftime("%H", gmtime())))

for stop in stops:
 fullurl = URL + apicmd + APIKEY + stop
 getPred(fullurl)

print "</pre>"
print """
<FORM>
<INPUT TYPE="button" onClick="history.go(0)" VALUE="Refresh">
</FORM>
"""
