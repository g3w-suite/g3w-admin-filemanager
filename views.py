from django.conf import settings
from django.views.generic import TemplateView, View
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from usersmanage.decorators import user_passes_test_or_403
from filemanager import FileManager
import json
import os


class FilemanagerView(TemplateView):

    template_name = 'filemanager/filemanager.html'

    @method_decorator(user_passes_test_or_403(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(FilemanagerView, self).dispatch(*args, **kwargs)


class FilemanagerServeConfigView(View):

    @method_decorator(user_passes_test_or_403(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(FilemanagerServeConfigView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/RichFilemanager/config/')
        file = open('{}{}'.format(path, kwargs['file_js']), 'r')
        config = json.load(file)
        file.close()

        # get current language
        config['language']['default'] = request.LANGUAGE_CODE
        return JsonResponse(config)


@csrf_exempt
@user_passes_test_or_403(lambda u: u.is_superuser)
def files_view(request):
    '''
    File Manager API endpoint
    '''

    try:
        if settings.FILEMANAGER_ROOT_PATH.endswith('/'):
            root_folder = settings.FILEMANAGER_ROOT_PATH[:-1]
        else:
            root_folder = settings.FILEMANAGER_ROOT_PATH
    except:
        if settings.DATASOURCE_PATH.endswith('/'):
            root_folder = settings.DATASOURCE_PATH[:-1]
        else:
            root_folder = settings.DATASOURCE_PATH

    fileManager = FileManager(request, root_folder=root_folder)

    mode = None
    if request.method == 'POST':
        if 'mode' in request.POST:
            mode = request.POST.get('mode')
    else:
        if 'mode' in request.GET:
            mode = request.GET.get('mode')
    return getattr(fileManager, mode, 'error')()

