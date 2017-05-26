#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

print " [Status] REDUCE"

lastReadedUserId = None
lastReadedCount = 0
separator = ","
fixed_data_length = 2

for line in sys.stdin:
  data_mapped = line.strip().split(separator)
  if len(data_mapped) != fixed_data_length:
    continue
  user_id, post_count = data_mapped
  if lastReadedUserId and lastReadedUserId != user_id:
    print lastReadedUserId, "\t", lastReadedCount
    lastReadedCount = 0
  lastReadedUserId = user_id
  lastReadedCount += int(post_count)

if lastReadedUserId:
  print lastReadedUserId, "\t", lastReadedCount


