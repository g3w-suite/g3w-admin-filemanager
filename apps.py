# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class FilemanagerConfig(AppConfig):
    name = 'filemanager'

    def ready(self):
        from django.conf import settings
        import filemanager_settings
        for a in dir(filemanager_settings):
            if not a.startswith('__') and not hasattr(settings, a):
                if not hasattr(settings, a):
                    setattr(settings, a, getattr(filemanager_settings, a))

