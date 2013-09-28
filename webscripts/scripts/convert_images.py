#!/usr/bin/env python

from pydub import AudioSegment
from pydub.utils import db_to_float
import argparse
import os
import Image

#Overall info goes here.
___overview___ = {
	'title': "Convert Image Files",
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
		'--ext', help='ext to output too')
	
	args=parser.parse_args()
	
	file_name = args.filename
	ext = args.ext

	im = Image.open(file_name)
	new_file_name_base = os.path.splitext(os.path.basename(file_name))[0]

	# save the result
	output_file_name = str(new_file_name_base + '.' + ext)
	im.save(output_file_name)




if __name__ == '__main__':
	script()



#Expand num of scripts with parameter options
def expand_infos():
	input_types = ['bmp', 'dcx', 'eps', 'ps', 'gif', 'im', 'jpg', 'jpe', 'jpeg',
				   'pcd', 'pcx', 'pdf', 'png', 'pbm', 'pgm', 'ppm', 'psd', 'tif', 'tiff',
				   'xbm', 'xpm']
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