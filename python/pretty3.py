#!/usr/bin/python
# -*- coding: UTF-8 -*-
# CTA API CLI YAH

import sys, requests, datetime
from xmltodict import parse
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

# timeStamp, Type, StopName, StopID, VehicleID, DestinationToStop, Route, RouteDirection, Destination, PredictionTime
showResponse = ["tmstmp","typ","stpnm","stpid","vid","dstp","rt","rtdir","des","prdtm"]
humanResponse = {"tmstmp":"Time","typ":"Type","stpnm":"StopName","stpid":"Stop #","vid":"VehicleID","dstp":"Distance","rt":"Route","rtdir":"Direction","des":"Destination","prdtm":"PredTime",}

def getPred(localurlx):
	print "getPred(" + str(localurlx) + ") called"
	localurl = URL + apicmd + APIKEY + stops[localurlx]
	r = requests.get(localurl)
	out = parse(r.text)
        ## Detect error  TODO: No arrival times still provides rt, stpid, msg  we should scrape thse out too
	if "error" in out['bustime-response']:
		#print "+" + str(out) + "+"
		#print "localurl: " + str(localurl)
		print "xXxXxXx\nERROR: " + out['bustime-response']['error']['msg']
		print type(out['bustime-response']['error']['msg'])
		print "xXxXxXx\n"
		bus.append(out['bustime-response']['error']['msg'])
		#sys.exit(1)
		return
	print "___"
	# Lame safety check:
	if "prdtm" in out['bustime-response']['prd']:
		for x in showResponse:
			print x + ": " + out['bustime-response']['prd'][x]
			thisBus = list()
			thisBus.append(out['bustime-response']['prd'][x])
		bus.append(thisBus)
	# true == multiple predictions returned
	if isinstance(out['bustime-response']['prd'], list):
		for x in range(0,len(out['bustime-response']['prd'])):
			if out['bustime-response']['prd'][x]:
				hourNow=int(out['bustime-response']['prd'][x]['tmstmp'][9:11])
				minNow=int(out['bustime-response']['prd'][x]['tmstmp'][12:14])
				hourPred=int(out['bustime-response']['prd'][x]['prdtm'][9:11])
				minPred=int(out['bustime-response']['prd'][x]['prdtm'][12:14])
				timeRemain = ((hourPred*60)+minPred) - ((hourNow*60)+minNow)
				thisBus = list()
				for response in showResponse:
				#print response + ": " + out['bustime-response']['prd'][x][response]
					print humanResponse[response] + ": " + out['bustime-response']['prd'][x][response]
					thisBus.append(out['bustime-response']['prd'][x][response])
				#print "Minutes remaining: " + str(timeRemain)
				#print "__thisBUS BEFORE   " , thisBus
				thisBus.append(timeRemain)
				#print "__thisBUS BEFORE   " , thisBus
				#print "__BUS BEFORE   " , bus
				bus.append(thisBus)
				#print "__BUS AFTER   " , bus
				#print "___"
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
			thisBus.append(timeRemain)
			bus.append(thisBus)
# --- getPred -----------------------------------------------------------------------------------------------------------

# Determine direction based on time of day
if int(strftime("%H", gmtime())) > 18 or int(strftime("%H", gmtime())) < 6 :
	# Heading home
	heading = "home"
	stops = ["&rt=78&stpid=11401", "&rt=56&stpid=14101"]
else:
	# heading to work
	heading = "work"
	stops = ["&rt=78&stpid=11321", "&rt=56&stpid=5586"]

# DEBUG OVER RIDE
stops = ["&rt=8&stpid=15274", "&rt=8&stpid=5790", "&rt=56&stpid=5586", "&rt=56&stpid=14101", "&rt=78&stpid=11401", "&rt=78&stpid=11321"]
stops = ["&rt=8&stpid=15274", "&rt=8&stpid=5790", "&rt=56&stpid=5586"]


route = list()

for x in range(0, len(stops)):
	bus = list()
	#fullurl = URL + apicmd + APIKEY + stops[x]
	getPred(x)
	route.append(bus)

print """Content-type: text/html
<html><title> Bus times - Heading to """ + heading + """</title><head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head><body><center>
"""


#<FORM>
#<INPUT TYPE="button" onClick="history.go(0)" VALUE="Refresh">
#</FORM>

#print "FUCK THIS : " + str(bus) + " : FUCK"
#for x in route:
#	print x
#	print "AAAA"
#
print route
