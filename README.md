scripts
=======

Making small python scripts into useful web services.  (eg. convert images, audio)

Demo:  http://webscripts.tonkworks.com



Installation:

Dependencies:
django

Dependencies for included scripts:
ffmpeg (http://www.ffmpeg.org/)
beautifulsoup
pydub
youtube-dl


To run:python manage.py runserver 0.0.0.0:80


To add new scripts - add the .py file to the /webscripts/scripts folder.  
When the server is restarted, it will detect the info supplied in the files __info__
and populate the webpage.
