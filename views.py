from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from usersmanage.decorators import user_passes_test_or_403
from filemanager import FileManager


class FilemanagerView(TemplateView):

    template_name = 'filemanager/filemanager.html'

    @method_decorator(user_passes_test_or_403(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(FilemanagerView, self).dispatch(*args, **kwargs)


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

