#!/usr/bin/env python

import urllib2
from BeautifulSoup import BeautifulSoup
import argparse


#Script Info goes here.
__info__ = [{
	'title': "Get Sun Rise Dates",
	'author': "Kevin Dagostino",
}]



#And the actual script.
def script():
	soup = BeautifulSoup(urllib2.urlopen('http://www.timeanddate.com/worldclock/astronomy.html?n=78').read())

	for row in soup('table', {'class': 'spad'})[0].tbody('tr'):
	    tds = row('td')
	    print tds[0].string, tds[1].string
	    # will print date and sunrise


if __name__ == '__main__':
	script()
