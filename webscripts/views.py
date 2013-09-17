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
    '''Get list of all python files in /scripts folder'''

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
                for i in info:
                    i['script_name'] = f

                    if 'image' not in i:
                        i['image'] = 'default.png'
                    scripts.append(i)

get_scripts()
root_path = os.path.dirname(os.path.realpath(__file__))

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



def CommandHandler(request, operation_uuid=None, input_file=None):
#    if request.method == 'POST':
        # try:
            if not operation_uuid:
                operation_uuid = str(uuid.uuid4())


            title = request.GET.get("script_name", default=None)
            #file_path = request.GET.get("input_file", default=None)

            s = get_script_by_title(title)
            print s
            input_script = s['script_name']
            
            parameters = request.GET.get("input_parameters", '')
            print parameters

            if 'parameters' in s:
                parameters = s['parameters'] + " " + parameters
            #Determine Script to use
            #Use script
            #input_file = file_path
            input_script = os.path.join(root_path, "scripts", input_script)
            bin_dir = os.path.join(root_path, "bin", operation_uuid) #TODO make folder with id .. grab everything in that folder

            if not os.path.exists(bin_dir):
                os.makedirs(bin_dir)

            if input_file:
                parameters = "\"{0}\" {1}".format(input_file, parameters)
            command = "python \"{0}\" {1}".format(input_script, parameters)

            logging.info(command)


            output = []
            output.append(parameters)

            output.append(command)
            p =subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=bin_dir)
            for line in p.stdout.readlines():
                logging.info(line)
                output.append(line)
            retval = p.wait()



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
        #   print e

        #     response = HttpResponse()
        #     response.content = json.dumps(e)
            
        #     return response

def FileUploadHandler(request):
#    if request.method == 'POST':
        # try:
            # print 'aaaa'
            # title = request.GET.get("script_name", default=None)

            # s = get_script_by_title(title)
            # print s
            # input_script = s['script_name']
            
            # parameters = ''
            # if 'parameters' in s:
            #     parameters = s['parameters']

            #Upload the file into the uploads directory
            print request.FILES

            f = request.FILES['file']
            original_fname = f.name            
            operation_uuid = str(uuid.uuid4())


            #final_filename= operation_uuid+extension

            upload_dir_path =  os.path.join(root_path, "uploads", operation_uuid)
            file_path =  os.path.join(upload_dir_path, original_fname)

            if not os.path.exists(upload_dir_path):
                os.makedirs(upload_dir_path)

            output_file = open(file_path, 'wb')
            output_file.write(f.read())
            output_file.close()

            return CommandHandler(request, operation_uuid, file_path)
            # #self.finish("file" + final_filename + " is uploaded")
            # #logging.info(f['body'])
            # #logging.info("file" + final_filename + " is uploaded")


            # #Determine Script to use
            # #Use script
            # input_file = file_path
            # input_script = os.path.join(os.getcwd(), "webscripts", "scripts", input_script)
            # bin_dir = os.path.join(os.getcwd(), "webscripts", "bin", operation_uuid) #TODO make folder with id .. grab everything in that folder

            # if not os.path.exists(bin_dir):
            #     os.makedirs(bin_dir)

            # command = "python \"{0}\" \"{1}\" {2}".format(input_script, input_file, parameters)
            # logging.info(command)


            # output = []
            # output.append(command)
            # p =subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=bin_dir)
            # for line in p.stdout.readlines():
            #     logging.info(line)
            #     output.append(line)
            # retval = p.wait()



            # from os import listdir
            # from os.path import isfile, join
            # files = [ f for f in listdir(bin_dir) if isfile(join(bin_dir,f)) ]

            # logging.info("files", files)

            # data = {
            #     'operation_uuid': operation_uuid,
            #     'number_of_files': len(files),
            #     'output': output
            # }
            # response = HttpResponse()
            # response.content = json.dumps(data)

            # return response

        # except Exception, e:
        # 	print e

        #     response = HttpResponse()
        #     response.content = json.dumps(e)
            
        #     return response
