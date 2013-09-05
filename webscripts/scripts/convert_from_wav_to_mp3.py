#!/usr/bin/env python

from pydub import AudioSegment
from pydub.utils import db_to_float
import argparse


#Script Info goes here.
__info__ = {
	'title': "Convert .wav to .mp3",
	'author': "Kevin Dagostino",
	'description': 'Convert an audio file from the wav format to the mp3 codec',
	'file_input': True,
	'image': 'Website Optimization.png'
}



#And the actual script.
def script():
	parser=argparse.ArgumentParser()
	parser.add_argument(
		'filename', help='a file name')
	args=parser.parse_args()
	file_name = args.filename


	# Let's load up the audio we need...
	audio_input = AudioSegment.from_wav(file_name)


	# save the result
	output_file_name = str('aoutput' + '.mp3')
	audio_input.export(output_file_name, format="mp3")

	print 'File has been MP3ed'




if __name__ == '__main__':
	script()
