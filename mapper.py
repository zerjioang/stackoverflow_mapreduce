#!/usr/bin/python

import sys
from xml.etree import ElementTree as ET

tag = 'OwnerUserId'
score_tag = 'Score'
user_id = None
min_score = 10

#parse stdin xml data
root = ET.parse(sys.stdin).getroot()
#get all rows
rows = root.findall('row')
#iterate
print " [Status] MAP"
for row in rows:
	uid = row.get(tag)
	score = row.get(score_tag)
	if int(score) > min_score:
		#print item as key value pair separated by comma
		print "{0},1".format(uid)

