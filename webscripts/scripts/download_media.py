#!/usr/bin/env python

import urllib2
import urllib
from BeautifulSoup import BeautifulSoup
import argparse
import os
import subprocess
import sys

from pydub import AudioSegment
from pydub.utils import db_to_float

#Overall info goes here.
___overview___ = {
    'title': "Download Media from web",
}

#Script Info goes here.
__info__ = [
]



#And the actual script.
def script():
    parser=argparse.ArgumentParser()
    parser.add_argument(
        'site_url', help='site_url')
    parser.add_argument(
        '--video_format', help='convert to video format', default='mp4')
    parser.add_argument(
        '--audio_format', help='convert to audio format as well', default=None)
    args=parser.parse_args()
    site_url = args.site_url


    video_format = args.video_format
    audio_format = args.audio_format



    command = ''
    if sys.platform == 'win32':
        command = "youtube-dl.exe {0} -f {1}".format(site_url, video_format)
    else:
        command = "youtube-dl {0} -f {1}".format(site_url, video_format)

    print command
    p =subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line
    retval = p.wait()

    if audio_format:
        #Get all mp4 files in bin.
        for f in os.listdir(os.getcwd()):
            print
            if '.mp4' in f:
                fileName, fileExtension = os.path.splitext(f) 
                audio_input = AudioSegment.from_file(f, 'mp4')
                output_file_name = str(fileName + '.' + audio_format)
                audio_input.export(output_file_name, format=audio_format)

                print output_file_name

if __name__ == '__main__':
    script()




#Expand num of scripts with parameter options
def expand_infos():
    websites = ['youtube', 'google video', 'google.com/videohp', 'photobucket.com',
                'yahoo.com', 'dailymotion', 'depositfiles', 'blip.tv', 'vimeo', 'myvideo.de',
                'www.thedailyshow.com', 'www.colbertnation.com', 'www.escapistmagazine.com', 'CollegeHumor', 'arte.tv',
                'Soundcloud', 'infox', 'mixcloud', 'Stanford Open Content', 'Youku', 'MTV',
                'xvideos', 'xnxx', 'google plus'
    ]
    output_types_words = ['video', 'audio', 'sound']
    output_types_ext = ['flv', '3gp', 'mp4', 'webm', 'mp3']
    for i in websites:
        for j in output_types_words:
            info = {
                'title': "Download a {0} file from {1}".format(j, i),
                'author': "Kevin Dagostino",
                'input': {
                    'label': 'url',
                }
            }

            if j == 'audio' or j == 'sound':
                info['parameters'] = '--audio_format=mp3'
            __info__.append(info)

    for i in websites:
        for j in output_types_ext:
            info = {
                'title': "Download a .{0} file from {1}".format(j, i),
                'author': "Kevin Dagostino",
                'input': {
                    'label': 'url',
                }
            }
            if j == 'wav' or j == 'mp3':
                info['parameters'] = '--audio_format=true'
            else:
                info['parameters'] = '--video_ext={0}'.format(j)

            __info__.append(info)


expand_infos()
