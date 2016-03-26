#!/usr/bin/python
#
# Playing with /proc/net/dev
#  Let's parse, digest and maybe even store it
#
# 03/26/2016 12am ver 0.1
#

#unit scale
unit = { 1: "KiB", 2: "MiB", 3: "GiB", 4: "TiB", 5: "PiB" }

print str(round(81287340600./1024/1024/1024,4))+" GiB"

b=81287340600	# user input eventually
d=2		# decimal

for m in unit.keys():
	print str(round(b/(1024**float(m)),d)), unit[m]

