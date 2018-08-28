#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-08-23
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [ocp7](http://github.com/freezed/ocp7/) project.

"""
from os import environ

PORT = 1664
HOST = '192.168.1.70'
APP = {
    'NAME': 'GrandPy Bot, le papy-robot',
    'SRC': 'http://github.com/freezed/ocp7/',
    'DEBUG': True,
}
GOO_API = {
    'URL_GEO': 'https://maps.googleapis.com/maps/api/geocode/json?',
    'URL_MAP': 'https://maps.googleapis.com/maps/api/staticmap?',
    'KEY': environ['GOO_API_KEY'],
    'MAP_SIZE': (600,300),
}
WIK_API = {
    'URL_SEARCH': 'https://fr.wikipedia.org/w/api.php?action=query&list=search&utf8=&format=json',
    'URL_ARTICL': 'https://fr.wikipedia.org/w/api.php?action=query&prop=extracts&exlimit=1&explaintext&utf8=&format=json',
    'LEN': 3,
}
