from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from .views import FilemanagerView, files_view

urlpatterns = [
    url(r'^$', login_required(FilemanagerView.as_view()), name='filemanager-home'),
]
