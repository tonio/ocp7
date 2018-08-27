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


class Place:
    """
    Place create a place with the parsed user query

    """

    def __init__(self, query, app_config):
        """
        Constructor
        """
        self.query = str(query)
        self.app_config = app_config
        self._country = "FR"

        self.filtered_data = self.goo_geocode()

    def goo_geocode(self):
        """
        Calls Google geocode API with a string query & retrieve a Place

        Filter API's JSON to keep only useful data
        """
        # Build URL request
        payload = {
            'key': self.app_config['GOO_API']['KEY'],
            'address': self.query,
            'region': self._country,
            'country': self._country,
        }

        response = requests.get(
            self.app_config['GOO_API']['URL_GEO'],
            payload,
        )

        api_json = json.loads(response.text)
        api_status = response.status_code

        if api_status != 200 or api_json['status'] != 'OK':
            print('API response status : {}'.format(api_status))

        # No data if request ĥas less or more 1 result
        if len(api_json['results']) != 1:
            filtered_data = {'not_single': True}

        else:
            # Dict aliases for smaller lines
            alias_ac = api_json['results'][0]['address_components']
            alias_go = api_json['results'][0]
            alias_vp = api_json['results'][0]['geometry']['viewport']

            filtered_data = {'truncated_address': [
                {alias_ac[1]['types'][0]: alias_ac[1]['long_name']},
                {alias_ac[2]['types'][0]: alias_ac[2]['long_name']},
                {alias_ac[3]['types'][0]: alias_ac[3]['long_name']},
                {alias_ac[4]['types'][0]: alias_ac[4]['long_name']}
            ]}

            filtered_data['formatted_address'] = alias_go['formatted_address']
            filtered_data['location'] = alias_go['geometry']['location']
            filtered_data['viewport_ne'] = alias_vp['northeast']
            filtered_data['viewport_sw'] = alias_vp['southwest']

        return filtered_data

    def get_static_map_url(self):
        """
        Return url of a static maps using Google Static Maps API
        """
        center = self.filtered_data['formatted_address']

        payload = {
            'key': self.app_config['GOO_API']['KEY'],
            'center': center,
            'markers': center,
            'size': "{}x{}".format(*self.app_config['GOO_API']['MAP_SIZE']),
        }

        response = requests.get(
            self.app_config['GOO_API']['URL_MAP'],
            payload,
        )

        return response.url
