#!/usr/bin/env python

from pydub import AudioSegment
from pydub.utils import db_to_float
import argparse
import os
import sys
import subprocess

#Overall info goes here.
___overview___ = {
	'title': "Convert Audio files",
}

#Function Info goes here.
__info__ = [
{
	'title': "Convert .mp3 to .wav",
	'author': "Kevin Dagostino",
	'description': 'Convert an audio file from the mp3 codec to the wav format',
	'file_input': True,
	'image': 'Custom Coding.png',
	'parameters': '--ext=wav'
}
]



#And the actual script.
def script():
    parser=argparse.ArgumentParser()
    parser.add_argument(
    	'filename', help='a file name')
    parser.add_argument(
    	'--ext', help='ext to output too')
    args=parser.parse_args()
    file_name = args.filename
    ext = args.ext

    new_file_name_base = os.path.splitext(os.path.basename(file_name))[0]
    output_file_name = str(new_file_name_base + '.' + ext)

    if sys.platform == 'win32':
        command = 'ffmpeg.exe -i "{0}" "{1}"'.format(file_name, output_file_name)
    else:
        command = 'ffmpeg -i "{0}" "{1}"'.format(file_name, output_file_name)

    print command
    p =subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print line
    retval = p.wait()


if __name__ == '__main__':
	script()




#Expand num of scripts with parameter options
def expand_infos():
	input_types = ['3gp', 'act', 'aiff', 'aac', 'alac', 'amr', 'atrac', 'au', 'awb', 
				   'dct', 'dss', 'dvf', 'flac', 'gsm', 'iklax', 'ivs', 'm4a', 'm4p', 
				   'mp3', 'mpc', 'msv', 'ogg', 'opus', 'raw', 'tta', 'vox', 'wav', 
				   'wma']
	output_types = ['3gp', 'act', 'aiff', 'aac', 'alac', 'amr', 'atrac', 'au', 'awb', 
				   'dct', 'dss', 'dvf', 'flac', 'gsm', 'iklax', 'ivs', 'm4a', 'm4p', 
				   'mp3', 'mpc', 'msv', 'ogg', 'opus', 'raw', 'tta', 'vox', 'wav', 
				   'wma']
	for i in input_types:
		for j in output_types:
			if i != j:
				info = {
					'title': "Convert .{0} to .{1}".format(i, j),
					'author': "Kevin Dagostino",
					'file_input': True,
					'parameters': '--ext={0}'.format(j)
				}
				__info__.append(info)

expand_infos()