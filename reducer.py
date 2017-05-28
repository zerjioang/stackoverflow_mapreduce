#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

print " [Status] REDUCE"

lastReadedUserId = None
lastReadedCount = 0
mapper_separator = ","
fixed_data_length = 2

for line in sys.stdin:
  # read standard input line
  data_mapped = line.strip().split(mapper_separator)
  #check data length, always must be len = 2 
  if len(data_mapped) != fixed_data_length:
    # skip received data
    continue
  # save received data in each variable
  user_id, post_count = data_mapped
  if lastReadedUserId != None and lastReadedUserId != user_id:
    print lastReadedUserId, "\t", lastReadedCount
    lastReadedCount = 0
  lastReadedUserId = user_id
  lastReadedCount += int(post_count)

if lastReadedUserId:
  print lastReadedUserId, "\t", lastReadedCount


