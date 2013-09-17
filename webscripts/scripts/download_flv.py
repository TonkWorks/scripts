#!/usr/bin/env python

import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
import argparse
import os
import subprocess
import sys

#Script Info goes here.
__info__ = [
{
    'title': "Download videos from youtube",
    'author': "Kevin Dagostino",
    'input': {
        'label': 'url',
    }
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

    command = ''
    if sys.platform == 'win32':
        command = "youtube-dl.exe {0}".format(site_url)
    else:
        command = "youtube-dl {0}".format(site_url)

    print command
    p =subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line
    retval = p.wait()



if __name__ == '__main__':
    script()
