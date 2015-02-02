#!/usr/bin/python
# -*- coding: UTF-8 -*-
# CTA API CLI YAH

import sys
import requests
from bs4 import BeautifulSoup
from xmltodict import parse
import datetime
# enable debugging
import cgitb
cgitb.enable()

#print "Content-Type: text/plain;charset=utf-8"
print "<html><title>CTA for Ray</title><body>"
print

# get API key from file
f = open('./.cta-api.key', 'r')
APIKEY = "?key=" + f.read(25)
f.close()

URL="http://www.ctabustracker.com/bustime/api/v1/"

apicmdOK = ["gettime", "getvehicles", "getroutes", "getdirections", "getstops", "getpatterns", "getpredictions", "getservicebulletins"]

# if two arguments aren't given fall back to just gettime
if len(sys.argv) <2:
 apicmd =  "getpredictions"
 apiargv = "&rt=78&stpid=11321"
 #apicmd = "gettime"
 #apiargv = ""
else:
 apicmd = sys.argv[1]
 #print "apicmd: " + apicmd
 apiargv = sys.argv[2]
 #print "apiargv: " + apiargv

if apicmd not in apicmdOK:
 print "you provided an invalid API command!"
 print "\nValid commands:"
 for x in apicmdOK:
  print "\t" + x
 sys.exit(1)


## print "URL: " + URL + apicmd + APIKEY + apiargv

# sys.exit()
r = requests.get(URL + apicmd + APIKEY + apiargv)


#print "r == " + str(r)
#print r.text
#soup = BeautifulSoup(r.text)
#print soup
out = parse(r.text)
#print "out ::"
#print out
##print '<tabletyle="width:100%">'
##print "<tr><td>___"
#print out['bustime-response']['']
#print out['bustime-response'][u'ptr'].keys()
if "error" in out['bustime-response']:
 print "+" + str(out) + "+"
 print "ERROR: " + out['bustime-response']['error']['msg']
 sys.exit(1)

# Lame safety check:
if "prdtm" in out['bustime-response']['prd']:
 #print "tmpstmp: " + out['bustime-response']['prd']['tmstmp']
 for x in ["tmstmp","typ","stpnm","stpid","vid","dstp","rt","rtdir","des","prdtm"]:
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
   for response in ["tmstmp","typ","stpnm","stpid","vid","dstp","rt","rtdir","des","prdtm"]:
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
# timeRemain = ((out['bustime-response']['prd']['prdtm'][9:11]*60) + out['bustime-response']['prd']['prdtm'][12:14]) - ((out['bustime-response']['prd']['tmstmp'][9:11]*60) + out['bustime-response']['prd']['tmstmp'][12:14])
#print out['bustime-response'].keys()
#print out['bustime-response']['tm']

#print APIKEY
# if two arguments aren't given fall back to just gettime
if len(sys.argv) <2:
 apicmd =  "getpredictions"
 apiargv = "&rt=56&stpid=5586&"
 #apicmd = "gettime"
 #apiargv = ""
else:
 apicmd = sys.argv[1]
 #print "apicmd: " + apicmd
 apiargv = sys.argv[2]
 #print "apiargv: " + apiargv

if apicmd not in apicmdOK:
 print "you provided an invalid API command!"
 print "\nValid commands:"
 for x in apicmdOK:
  print "\t" + x
 sys.exit(1)


## print "URL: " + URL + apicmd + APIKEY + apiargv

# sys.exit()
r = requests.get(URL + apicmd + APIKEY + apiargv)

#print "r == " + str(r)
#print r.text
#soup = BeautifulSoup(r.text)
#print soup
out = parse(r.text)
#print "out ::"
#print out
print "___<td>"
#print out['bustime-response']['']
#print out['bustime-response'][u'ptr'].keys()
if "error" in out['bustime-response']:
 print "+" + str(out) + "+"
 print "ERROR: " + out['bustime-response']['error']['msg']
 sys.exit(1)

# Lame safety check:
if "prdtm" in out['bustime-response']['prd']:
 #print "tmpstmp: " + out['bustime-response']['prd']['tmstmp']
 for x in ["tmstmp","typ","stpnm","stpid","vid","dstp","rt","rtdir","des","prdtm"]:
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
   for response in ["tmstmp","typ","stpnm","stpid","vid","dstp","rt","rtdir","des","prdtm"]:
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
# timeRemain = ((out['bustime-response']['prd']['prdtm'][9:11]*60) + out['bustime-response']['prd']['prdtm'][12:14]) - ((out['bustime-response']['prd']['tmstmp'][9:11]*60) + out['bustime-response']['prd']['tmstmp'][12:14])
#print out['bustime-response'].keys()
#print out['bustime-response']['tm']
print "</tr></table>"
#print APIKEY
