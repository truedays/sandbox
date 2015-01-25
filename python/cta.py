#!/usr/bin/python
# ray@truedays.org
# CTA API CLI YAH

import sys
import requests
from bs4 import BeautifulSoup
from xmltodict import parse


# get API key from file
f = open('./.cta-api.key', 'r')
APIKEY = "?key=" + f.read(25)
f.close()

URL="http://www.ctabustracker.com/bustime/api/v1/"

apicmdOK = ["gettime", "getvehicles", "getroutes", "getdirections", "getstops", "getpatterns", "getpredictions", "getservicebulletins"]


if len(sys.argv) <2:
# apicmd = "getpredictions"
# apiargv = "&rt=20&stpid=456"
 apicmd = "gettime"
 apiargv = ""
else:
 apicmd = sys.argv[1]
 print "apicmd: " + apicmd
 apiargv = sys.argv[2]
 print "apiargv: " + apiargv

if apicmd not in apicmdOK:
 print "you provided an invalid API command!"
 print "\nValid commands:"
 for x in apicmdOK:
  print "\t" + x
 sys.exit(1)


print URL + apicmd + APIKEY + apiargv

# sys.exit()
r = requests.get(URL + apicmd + APIKEY + apiargv)



#print "r == " + str(r)
print r.text
#soup = BeautifulSoup(r.text)
#print soup
out = parse(r.text)
#print "out ::"
#print out
print "___"
#print out['bustime-response']['']
#print out['bustime-response'][u'ptr'].keys()
#print "tmpstmp: " + out['bustime-response']['prd']['tmstmp']
for x in ["tmstmp","typ","stpnm","stpid","vid","dstp","rt","rtdir","des","prdtm"]:
 print x + ": " + out['bustime-response']['prd'][x] 
 #out['bustime-response']['prd']:
 #print key
 #print x
print "___"

#print out['bustime-response'].keys()
#print out['bustime-response']['tm']

#print APIKEY
