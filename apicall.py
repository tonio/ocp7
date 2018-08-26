#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-08-25
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [ocp7](http://github.com/freezed/ocp7/) project.

 """
import json
import requests
from config import GOO_API


def goo_geocode(query="open classrooms", country='FR'):
    """
    Function documentation
    """

    payload = {
        'key': GOO_API['KEY'],
        'address': query,
        'region': country,
        'country': country,
    }

    response = requests.get(
        GOO_API['URL_GEO'],
        payload,
    )
    api_json = json.loads(response.text)
    api_status = response.status_code

    if api_status != 200 or api_json['status'] != 'OK':
        print('API response status : {}'.format(api_status))

    return api_json


if __name__ == "__main__":
    goo_geocode()
