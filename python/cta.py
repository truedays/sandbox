#!/usr/bin/python
# ray@truedays.org
# CTA API CLI YAH

import sys
import requests
from bs4 import BeautifulSoup



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

sys.exit()
r = requests.get(URL + apicmd + APIKEY + apiargv)




print r
print r.text
#soup = BeautifulSoup(r.text)
#print soup


#print APIKEY
