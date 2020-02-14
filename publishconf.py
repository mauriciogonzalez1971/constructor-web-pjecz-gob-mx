#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# Para producción los URLs son absolutos
SITEURL = 'https://pjecz.github.io/beta'
RELATIVE_URLS = False

# Para producción habilitar dependencias de otros servidores en Internet
USE_REMOTE_SERVICES = True

# Para producción se activa la generacion de feeds
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None
FEED_MAX_ITEMS = 24
RSS_FEED_SUMMARY_ONLY = True

# Para producción se habilita la paginación
DEFAULT_PAGINATION = True
DEFAULT_PAGINATION = 8
DEFAULT_ORPHANS = 2

# Para producción se habilitan los plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 1,
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly',
    },
    'exclude': [
        'archives.html',
        'tags.html',
        'categories.html',
        'author/',
    ],
}

# Para producción NO BORRAR todo el directorio de salida
DELETE_OUTPUT_DIRECTORY = True

# Para producción activar el caché
LOAD_CONTENT_CACHE = True