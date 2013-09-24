#!/usr/bin/env python

import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
import argparse
import os
#Overall info goes here.
___overview___ = {
    'title': "Web Scrapers",
}

#Function Info goes here.
__info__ = [
{
	'title': "Download all images from a web page",
	'author': "Kevin Dagostino",
	'input': {
		'label': 'url',
	},
	'parameters': '--find=img'
}
]



#And the actual script.
def script():
    parser=argparse.ArgumentParser()
    parser.add_argument(
    	'site_url', help='site_url')
    parser.add_argument(
    	'--find', help='files to scrap')
    args=parser.parse_args()
    site_url = args.site_url
    find = args.find

    soup = BeautifulSoup(urllib2.urlopen(site_url))
    parsed = list(urllib2.urlparse.urlparse(site_url))

    for image in soup.findAll(find):
        print "Image: %(src)s" % image

        filename = image["src"].split("/")[-1]
        parsed[2] = image["src"]
        outpath = os.path.join(os.getcwd(), filename)
        if image["src"].lower().startswith("http"):
            urllib.urlretrieve(image["src"], outpath)
        else:
            urllib.urlretrieve(urllib2.urlparse.urlunparse(parsed), outpath)


if __name__ == '__main__':
	script()
