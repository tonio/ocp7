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
from config import GOO_API, WIK_API


def get_json(url, payload):
    """
    Request API
    """
    response = requests.get(url, payload)
    api_json = response.json()
    api_status = response.status_code
    return (api_status, api_json)


class Article:
    """ Class doc """

    def __init__(self, query):
        """
        Class initialiser

        """
        self.query = query
        self.data = {'status': False}

    def get_data(self):
        """
        Function documentation

        """

        (search_status, search_json) = get_json(
            WIK_API['URL_SEARCH'],
            {'srsearch': self.query}
        )

        if 'search' not in search_json['query'] or search_status != 200:
            self.data['context'] = 'search'

        else:
            self.data['status'] = True
            self.data['title'] = search_json['query']['search'][0]['title']
            self.data['pageid'] = search_json['query']['search'][0]['pageid']

            (article_status, article_json) = get_json(
                WIK_API['URL_ARTICL'],
                {
                    'titles': self.data['title'],
                    'exsentences': 4,
                    # exintro,
                }
            )
            # import pdb; pdb.set_trace()

            if str(self.data['pageid']) not in article_json['query']['pages'] or article_status != 200:
                self.data['context'] = 'article'

            else:
                self.data['status'] = True
                self.data['extract'] = article_json['query']['pages'][str(self.data['pageid'])]['extract']

        return self.data['extract']


class Place:
    """
    Place create a place with the parsed user query

    """

    def __init__(self, query):
        """
        Constructor
        """
        self.query = str(query)
        self._country = "FR"

        self.filtered_data = self.goo_geocode()

    def goo_geocode(self):
        """
        Calls Google geocode API with a string query & retrieve a Place

        Filter API's JSON to keep only useful data
        """
        # Build URL request
        payload = {
            'key': GOO_API['KEY'],
            'address': self.query,
            'region': self._country,
            'country': self._country,
        }

        response = requests.get(
            GOO_API['URL_GEO'],
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
            'key': GOO_API['KEY'],
            'center': center,
            'markers': center,
            'size': "{}x{}".format(*GOO_API['MAP_SIZE']),
        }

        response = requests.get(
            GOO_API['URL_MAP'],
            payload,
        )

        return response.url
