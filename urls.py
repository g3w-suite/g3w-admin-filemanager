from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import *

'''
   
   url(r'^languages/(?P<file_js>[-_\.\\\w\d]+)$', login_required(FilemanagerServeLanguageView.as_view()),
       name='filemanager-serve-file-config'),
   url(r'^scripts/(?P<file>[-_\.\/\w\d]+)$', login_required(FilemanagerServeScriptView.as_view()),
       name='filemanager-serve-file-config'),
   '''

urlpatterns = [
    url(r'^$', login_required(FilemanagerView.as_view()), name='filemanager-home'),
    url(r'^config/(?P<file_js>[-_\.\\\w\d]+)$', login_required(FilemanagerServeConfigView.as_view()),
       name='filemanager-serve-file-config'),
]
