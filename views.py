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

    def get(self, request, *args, **kwargs):

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/RichFilemanager/config/')
        file = open('{}{}'.format(path, kwargs['file_js']), 'r')
        config = json.load(file)
        file.close()

        # try to change language
        return JsonResponse(config)

'''
class FilemanagerServeLanguageView(View):

    def get(self, request, *args, **kwargs):

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/RichFilemanager/languages/')
        file = open('{}{}'.format(path, kwargs['file_js']), 'r')
        return JsonResponse(json.load(file))



class FilemanagerServeScriptView(View):

    def get(self, request, *args, **kwargs):

        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/RichFilemanager/scripts/')
        file_js = kwargs['file']
        file = open('{}{}'.format(path, file_js), 'r')

        if file_js.endswith('.html'):
            return HttpResponse(file.read())
        else:
            return JsonResponse(json.load(file))
'''

@csrf_exempt
@user_passes_test_or_403(lambda u: u.is_superuser)
def files_view(request):
    '''
    File Manager API endpoint
    '''

    fileManager = FileManager(request, root_folder=settings.DATASOURCE_PATH[:-1])

    mode = None
    if request.method == 'POST':
        if 'mode' in request.POST:
            mode = request.POST.get('mode')
    else:
        if 'mode' in request.GET:
            mode = request.GET.get('mode')
    return getattr(fileManager, mode, 'error')()

