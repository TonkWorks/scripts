from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

import os

import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


ROOT_PATH = os.path.dirname(__file__)
STATICFILES_DIRS = [os.path.join(ROOT_PATH, 'media')]

BIN_DIR = os.path.join(os.getcwd(), "webscripts", "bin")

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'webscripts.views.home', name='home'),
    url(r'^script/(?P<script_name>.*)$', 'webscripts.views.script', name='script'),


    url(r'^api/save$', 'webscripts.views.APISaveHandler', name='api-save'),
    url(r'^api$', 'webscripts.views.APISaveHandler', name='api'),

    url(r"^postFile", 'webscripts.views.FileUploadHandler', name='file_handler'),
    url(r"^file", 'webscripts.views.FileServerHander', name='file_server_handler'),
    url(r'^bin/(?P<path>.*)$', 'django.views.static.serve',{'document_root': BIN_DIR, 'show_indexes': True}),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': STATICFILES_DIRS })
)
