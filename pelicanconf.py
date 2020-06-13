#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import collections
import six

AUTHOR = u'Mike Mallin'
SITENAME = u"Mike Mallin's Homepage"
SITEURL = ''

DISPLAY_ARTICLE_INFO_ON_INDEX = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = u'en'

THEME = os.getcwd() + '/theme/pelican-blueidea'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = [ os.getcwd() + '/plugins']
PLUGINS = ['autostatic', 'advthumbnailer', 'metadataparsing']

STATIC_PATHS = ['images', 'mco']

DEFAULT_PAGINATION = 10

# Borrowed from github.com/AlexJF/alexjf.net
GalleryItem = collections.namedtuple("GalleryItem", ["url", "description"])
def parse_gallery(string):
    if string is None or not isinstance(string, collections.Iterable):
        return None

    if not isinstance(string, six.string_types):
        string = '\n'.join(string)

    items = []
    
    for line in string.split('\n'):
        if not line:
            continue
        parts = line.split("||")
        url = parts[0].strip()
        if len(parts) == 1:
            description = None
        else:
            description = parts[1].strip()
        items.append(GalleryItem(url, description))
    return items

def parse_description(string):
    if string is None or isinstance(string, six.string_types):
        return string
    if isinstance(string, collections.Iterable):
        string = " ".join(string)
    return string

METADATA_PARSERS = {
    "Gallery": parse_gallery,
    "Description": parse_description,
}
