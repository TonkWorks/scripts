#!/usr/bin/env python

import argparse
import os
import sys
import subprocess

#Overall info goes here.
___overview___ = {
	'title': "Convert Video files",
}

#Function Info goes here.
__info__ = [
]



#And the actual script.
def script():
    parser=argparse.ArgumentParser()
    parser.add_argument(
    	'filename', help='a file name')
    parser.add_argument(
    	'--ext', help='ext to output to')
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
    input_types = ['3g2', '3gp', 'asf', 'asx', 'avi', 'flv', 'm4v', 'mov', 'mp4'
                   'mov', 'mp4', 'mpg', 'rm', 'srt', 'swf', 'vob', 'wmv']
    output_types = input_types
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