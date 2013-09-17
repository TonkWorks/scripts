from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

import os
import sys
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
if sys.platform == 'win32':
    ROOT_PATH = os.path.join(ROOT_PATH, 'webscripts')
STATICFILES_DIRS = [os.path.join(ROOT_PATH, 'media')]
SCRIPTS_DIR = os.path.join(ROOT_PATH, "scripts")
BIN_DIR = os.path.join(ROOT_PATH, "bin")

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'webscripts.views.home', name='home'),
    url(r'^script/(?P<script_name>.*)$', 'webscripts.views.script', name='script'),


    url(r'^api/save$', 'webscripts.views.APISaveHandler', name='api-save'),
    url(r'^api$', 'webscripts.views.APISaveHandler', name='api'),


    url(r"^command", 'webscripts.views.CommandHandler', name='command_handler'),
    url(r"^postFile", 'webscripts.views.FileUploadHandler', name='file_handler'),

    url(r'^scripts/(?P<path>.*)$', 'webscripts.static_views.serve',
        {'document_root': SCRIPTS_DIR, 'show_indexes': True}),

    
    url(r'^bin/(?P<path>.*)$', 'webscripts.static_views.serve',
        {'document_root': BIN_DIR, 'show_indexes': True}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': STATICFILES_DIRS })
)
