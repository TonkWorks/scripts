#!/usr/bin/env python

from pydub import AudioSegment
from pydub.utils import db_to_float
import argparse
import os

#Script Info goes here.
__info__ = [
{
	'title': "Convert .mp3 to .wav",
	'author': "Kevin Dagostino",
	'description': 'Convert an audio file from the mp3 codec to the wav format',
	'file_input': True,
	'image': 'Custom Coding.png',
	'parameters': '--ext=wav'
},
{
	'title': "Convert .mp3 to .aac",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=aac'
},
{
	'title': "Convert .mp3 to .aiff",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=aiff'
},
{
	'title': "Convert .mp3 to .flac",
	'author': "Kevin Dagostino",
	'file_input': True,
	'parameters': '--ext=flac'
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


	# Let's load up the audio we need...
	audio_input = AudioSegment.from_mp3(file_name)


	new_file_name_base = os.path.splitext(os.path.basename(file_name))[0]

	# save the result
	output_file_name = str(new_file_name_base + '.' + ext)
	print output_file_name


	audio_input.export(output_file_name, format="wav")

	print 'File has been WAVed'




if __name__ == '__main__':
	script()
