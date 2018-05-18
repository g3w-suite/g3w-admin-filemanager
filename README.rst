=================
G3W-ADMIN-FILEMANAGER
=================

G3W-ADMIN-FILEMANAGER is a files managment module.

Installation
------------

Add like git submodule from main g3w-admin directory

::

     git submodule add -f https://<user>@bitbucket.org/gis3w/g3w-admin-filemanager.git g3w-admin/filemanager


Add 'notes' module to G3WADMIN_LOCAL_MORE_APPS config value inside local_settings.py:

::

    G3WADMIN_LOCAL_MORE_APPS = [
        ...
        'filemanager'
        ...
    ]


Sync tree menu by manage.py:

::

    ./manage.py sitetree_resync_apps filemanager