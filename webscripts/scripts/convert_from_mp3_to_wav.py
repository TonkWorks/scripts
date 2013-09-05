#!/usr/bin/env python

from pydub import AudioSegment
from pydub.utils import db_to_float
import argparse


#Script Info goes here.
__info__ = {
	'title': "Convert .mp3 to .wav",
	'author': "Kevin Dagostino",
	'description': 'Convert an audio file from the mp3 codec to the wav format',
	'file_input': True,
	'image': 'Custom Coding.png'
}



#And the actual script.
def script():
	parser=argparse.ArgumentParser()
	parser.add_argument(
		'filename', help='a file name')
	args=parser.parse_args()
	file_name = args.filename


	# Let's load up the audio we need...
	audio_input = AudioSegment.from_mp3(file_name)


	# save the result
	output_file_name = str('aoutput' + '.wav')
	audio_input.export(output_file_name, format="wav")

	print 'File has been WAVed'




if __name__ == '__main__':
	script()
