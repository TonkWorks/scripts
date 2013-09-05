from __future__ import with_statement
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core import serializers
from django.core.servers.basehttp import FileWrapper


# -*- coding: utf-8 -*-

import sys
import imp
import logging
import json
import urllib

import re


import logging
import os.path
import uuid
import json
import random
import subprocess
import mimetypes
import sqlite3


scripts = []

def home(request):
	return render_to_response('webscripts/templates/index.html',
	        {
	        	'scripts': scripts
	        }
	)

def script(request, script_name):

	print script_name
	s = get_script_by_title(script_name)

	if not s:
		pass #TODO return 404

	print s

	return render_to_response('webscripts/templates/script.html',
	        {
	        	'script': s
	        }
	)



def get_scripts():
	#Get list of all python files in /scripts folder
	del scripts[:]


	root_path = os.path.dirname(__file__)
	scripts_path = os.path.join(root_path, 'scripts')

	sys.path.append(scripts_path)

	for f in os.listdir(scripts_path):
		ext = os.path.splitext(f)


		if ext[1] == '.py':
			module = __import__( ext[0] )

			if hasattr(module, '__info__'):
				info = module.__info__
				info['script_name'] = f
				scripts.append(module.__info__)

get_scripts()

def get_script_by_title(title):
	try:
		for x in scripts:
			if (x['title'] == title):
				return x
	except Exception, e:
		print e
		return None
def APISaveHandler(request):
    s = Script()
    s.script_name = request.GET.get("script_name", default=None)
    s.file_input = request.GET.get("file_input", default=False)
    s.description = request.GET.get("description", default=None)       

    s.save()
    data = {
        # 'script_name': script_name,
        # 'file_input': file_input,
        # 'description': description
        'script': ''

    }

    a = serializers.serialize('json', Script.objects.all())

    return HttpResponse(a, mimetype="application/json")


def API(request):
	    script_name = request.GET.get("script_name", default=None)
	    file_input = request.GET.get("file_input", default=False)
	    description = request.GET.get("description", default=None)       

	    data = {
	        'script_name': script_name,
	        'file_input': file_input,
	        'description': description
	    }
	    return HttpResponse(json.dumps(data), mimetype="application/json")

def FileUploadHandler(request):
#    if request.method == 'POST':
        # try:
            title = request.GET.get("script_name", default=None)

            s = get_script_by_title(title)
            print s
            input_script = s['script_name']

            #Upload the file into the uploads directory
            print request.FILES

            f = request.FILES['file']
            print f

            original_fname = f.name

            extension = os.path.splitext(original_fname)[1]
            
            operation_uuid = str(uuid.uuid4())




            final_filename= operation_uuid+extension

            file_path =  os.path.join(os.getcwd(), "webscripts", "uploads", final_filename)

            print file_path

            output_file = open(file_path, 'wb')
            output_file.write(f.read())
            output_file.close()


            #self.finish("file" + final_filename + " is uploaded")
            #logging.info(f['body'])
            #logging.info("file" + final_filename + " is uploaded")


            #Determine Script to use
            #Use script
            input_file = final_filename

            input_file = os.path.join(os.getcwd(), "webscripts", "uploads", input_file)
            input_script = os.path.join(os.getcwd(), "webscripts", "scripts", input_script)
            bin_dir = os.path.join(os.getcwd(), "webscripts", "bin", operation_uuid) #TODO make folder with id .. grab everything in that folder

            if not os.path.exists(bin_dir):
                os.makedirs(bin_dir)

            command = "python " + '"' + input_script + '"' + " " + '"' + input_file + '"'
            logging.info(command)


            output = []
            p =subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=bin_dir)
            for line in p.stdout.readlines():
                logging.info(line)
                output.append(line)
            retval = p.wait()



            #Return File
            
            # with open(output_file_path, 'rb') as f:
            #     while 1:
            #         data = f.read(16384) # or some other nice-sized chunk
            #         if not data: break
            #         self.write(data)
            # self.finish()


            from os import listdir
            from os.path import isfile, join
            files = [ f for f in listdir(bin_dir) if isfile(join(bin_dir,f)) ]

            logging.info("files", files)

            data = {
                'operation_uuid': operation_uuid,
                'number_of_files': len(files),
                'output': output
            }
            response = HttpResponse()
            response.content = json.dumps(data)

            return response

        # except Exception, e:
        # 	print e

        #     response = HttpResponse()
        #     response.content = json.dumps(e)
            
        #     return response




# def FileServerHander(request):
#         #Todo Delete?
#         id = request.GET.get('id')
#         if id:
#             #self.set_header('Content-Type', mimetypes.guess_type(id))


#             bin_dir = os.path.join(os.getcwd(), "webscripts", "bin", id)

#             from os import listdir
#             from os.path import isfile, join
#             files = [ f for f in listdir(bin_dir) if isfile(join(bin_dir,f)) ]

#             for f in files:
#                 print f

#                 output_file_path = os.path.join(bin_dir, f)
                
#                 extension = os.path.splitext(output_file_path)[1]
#                 filename = os.path.basename(output_file_path)
#                 response = HttpResponse(FileWrapper(open(output_file_path)),
#                                        content_type=mimetypes.guess_type(output_file_path)[0])
#                 response['Content-Length'] = os.path.getsize(output_file_path)    
#                 response['Content-Disposition'] = "attachment; filename=%s" % filename
#                 return response