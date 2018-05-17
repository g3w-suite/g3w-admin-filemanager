from sitetree.utils import item
from core.utils.tree import G3Wtree

# Be sure you defined `sitetrees` in your module.

'''
G3Wtree('filemanager', title='Filemanager', module='filemanager', items=[
  # Then define items and their children with `item` function.
  item('FILE MANAGER', '#', type_header=True),
  item('Files', 'filemanager-home', icon_css_class='fa fa-file', url_as_pattern=True),
]),

G3Wtree('filemanager_en', title='Filemanager', module='filemanager', items=[
    # Then define items and their children with `item` function.
    item('FILE MANAGER', '#', type_header=True),
    item('Files', 'filemanager-home', icon_css_class='fa fa-file', url_as_pattern=True),
]),
'''

sitetrees = (
    # Define a tree with `tree` function.
    G3Wtree('filemanager_sidebar_right', title='File Manager sidebar right', module='filemanager', items=[
        item('FILE MANAGER', '#', type_header=True),
        item('Files', 'filemanager-home', icon_css_class='fa fa-file'),
    ]),

    G3Wtree('filemanager_sidebar_right_en', title='STRESS navabar', module='filemanager', items=[
        item('FILE MANAGER', '#', type_header=True),
        item('Files', 'filemanager-home', icon_css_class='fa fa-file'),
    ]),
)

