#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CKI Project Team'
SITENAME = 'CKI Project'
SITEURL = ''
PATH = 'content'
TIMEZONE = 'Etc/UTC'
DEFAULT_LANG = 'en'

# Config for 'nice-blog' theme
THEME = 'themes/nice-blog'
THEME_COLOR = 'red'
SIDEBAR_DISPLAY = ['about', 'categories', 'tags']
SIDEBAR_ABOUT = "The CKI Project mission is to find bugs before they are committed to the Linux kernel."
COPYRIGHT = "CKI Project"
LOGO = 'cookie.png'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feed'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
