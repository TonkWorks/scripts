#!/usr/bin/env python

from pydub import AudioSegment
from pydub.utils import db_to_float
import argparse
import os
import Image

#Script Info goes here.
__info__ = [
{
	'title': "Convert to .bmp",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=bmp'
},
{
	'title': "Convert to .dcx",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=dcx'
},
{
	'title': "Convert to .eps",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=eps'
},
{
	'title': "Convert to .gif",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=gif'
},
{
	'title': "Convert to .im",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=im'
},
{
	'title': "Convert to .jpg",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=jpg'
},
{
	'title': "Convert to .jpeg",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=jpeg'
},
{
	'title': "Convert to .pcd",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=pcd'
},
{
	'title': "Convert to .pcx",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=pcx'
},
{
	'title': "Convert to .pdf",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=pdf'
},
{
	'title': "Convert to .png",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=png'
},
{
	'title': "Convert to .ppm",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=ppm'
},
{
	'title': "Convert to .psd",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=psd'
},
{
	'title': "Convert to .tiff",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=tiff'
},
{
	'title': "Convert to .xbm",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=xbm'
},
{
	'title': "Convert to .xpm",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=xpm'
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

	im = Image.open(file_name)
	new_file_name_base = os.path.splitext(os.path.basename(file_name))[0]

	# save the result
	output_file_name = str(new_file_name_base + '.' + ext)
	im.save(output_file_name)




if __name__ == '__main__':
	script()
