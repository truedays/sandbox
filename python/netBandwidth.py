#!/usr/bin/python
#
# Playing with /proc/net/dev
#  Let's parse, digest and maybe even store it
#
# 03/26/2016 12am ver 0.1
#

#unit scale
unit = { 1: "KiB", 2: "MiB", 3: "GiB", 4: "TiB", 5: "PiB" }

import sys
data = { 0:"bytes", 1:"packets", 2:"errors", 3:"drop", 4:"fifo", 5:"frame", 6:"compressed", 7:"multicast" }
interface = ""
recv = []
sent = []

i = [ interface, recv, sent ]

f = open('/proc/net/dev', 'r')
for line in f.readlines():
	if "Inter" in line:
		print "skipping.."
		continue
	if "bytes" in line:
		print "bytes detected in line, skipping.."
		continue
	print "__" + line
f.close()


print str(round(81287340600./1024/1024/1024,4))+" GiB"

b=81287340600	# user input eventually
d=2		# decimal

for m in unit.keys():
	print str(round(b/(1024**float(m)),d)), unit[m]

# $ grep -Ev 'Inter-\|| face \|bytes' /proc/net/dev |tr -d ':'	#Throwing away the header, here's a reference:
#
# Inter-|   Receive                                                |  Transmit
#  face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed

# i = { 0:"Interface", recv = { 0:"bytes", 2:"packets", 3:" 


