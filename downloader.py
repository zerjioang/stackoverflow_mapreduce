#!/usr/bin/python

import urllib
import urllib2
import sys
from xml.etree import ElementTree as ET

file_name = ''

def run(url):
	download_dataset(url)

def download_dataset(url):
	print 'Starting MapReduce on selected dataset\n'
	print 'Downloading data...\n'

	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading: %s Bytes: %s" % (file_name, file_size)

	file_size_dl = 0
	block_sz = 8192
	while True:
	    buffer = u.read(block_sz)
	    if not buffer:
		break

	    file_size_dl += len(buffer)
	    f.write(buffer)
	    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
	    status = status + chr(8)*(len(status)+1)
	    print status,

	f.close()

if __name__ == "__main__":
	#slower but more data
	url = "https://archive.org/download/stackexchange/unix.stackexchange.com.7z"
	#faster for testing
	url = "https://archive.org/download/stackexchange/chemistry.stackexchange.com.7z" 
	run(url)
