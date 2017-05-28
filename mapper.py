#!/usr/bin/python

import sys
from xml.etree import ElementTree as xml

main_root = 'row'
tag = 'OwnerUserId'
score_tag = 'Score'
min_score = 10

#parse stdin xml data
root = xml.parse(sys.stdin).getroot()

#get all rows
rows = root.findall(main_root)

#iterate
print " [Status] MAP"

for row in rows:
	uid = row.get(tag)
	score = row.get(score_tag)
	if int(score) > min_score and uid != None:
		#print item as key value pair separated by comma
		print "{0},1".format(uid)

