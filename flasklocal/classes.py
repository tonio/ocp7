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

class Place:
    """
    Defines a place with the user query

    Gets geo data from Google geocode & static map API
    Gets information from Wikipedia API

    """

    def __init__(self, query):
        """
        Sets arguments
        """
        self.query = str(query)
        self.article_data = {'status': False}

        # Get geodata
        self.set_geo_data()
        self.set_article_data()

    def get_json(self, url, payload):
        """
        Request API
        """
        response = requests.get(url, payload)
        api_json = response.json()
        api_status = response.status_code

        if response.status_code == 200:
            return api_json

        else:
            return False

    def set_article_data(self):
        """
        Function documentation

        """
        payload = {'srsearch': self.query}

        search_json = self.get_json(WIK_API['URL_SEARCH'], payload)

        try:
            self.article_data['title'] = search_json['query']['search'][0]['title']
            self.article_data['pageid'] = search_json['query']['search'][0]['pageid']

        except TypeError:
            self.article_data['context'] = 'search'

        else:
            self.article_data['status'] = True
            payload = {'titles': self.article_data['title'], 'exsentences': 4}

            article_json = self.get_json(WIK_API['URL_ARTICL'], payload)

            try:
                self.article_data['extract'] = article_json['query']['pages'][str(self.article_data['pageid'])]['extract']

            except TypeError:
                self.article_data['context'] = 'article'
                self.article_data['status'] = False

        # dev
        import pprint; pprint.pprint(self.article_data)

    def set_geo_data(self):
        """
        Calls Google geocode API with a string query & retrieve a Place

        Filter API's JSON to keep only useful data
        """
        # Build URL request
        payload = {
            'key': GOO_API['KEY'],
            'address': self.query,
            'region': GOO_API['COUNTRY'],
            'country': GOO_API['COUNTRY'],
        }

        geo_json = self.get_json(GOO_API['URL_GEO'],payload)

        try:
            # Dict aliases for smaller lines
            alias_ac = geo_json['results'][0]['address_components']
            alias_go = geo_json['results'][0]
            alias_vp = geo_json['results'][0]['geometry']['viewport']

            self.geo_data = {'truncated_address':
                {
                    alias_ac[1]['types'][0]: alias_ac[1]['long_name'],
                    alias_ac[2]['types'][0]: alias_ac[2]['long_name'],
                    alias_ac[3]['types'][0]: alias_ac[3]['long_name'],
                    alias_ac[4]['types'][0]: alias_ac[4]['long_name'],
                }
            }

            self.geo_data['formatted_address'] = alias_go['formatted_address']
            self.geo_data['location'] = alias_go['geometry']['location']
            self.geo_data['viewport_ne'] = alias_vp['northeast']
            self.geo_data['viewport_sw'] = alias_vp['southwest']

        except TypeError:
            self.geo_data = {'error': 'no_data'}

        else:
            # No data if request ĥas less or more 1 result
            if len(geo_json['results']) != 1:
                self.geo_data = {'warning': 'not_single'}

        # dev
        import pprint; pprint.pprint(self.geo_data)

    def get_static_map_url(self):
        """
        Return url of a static maps using Google Static Maps API
        """
        payload = {
            'key': GOO_API['KEY'],
            'center': self.geo_data['formatted_address'],
            'markers': self.geo_data['formatted_address'],
            'size': "{}x{}".format(*GOO_API['MAP_SIZE']),
        }

        response = requests.get(
            GOO_API['URL_MAP'],
            payload,
        )

        return response.url
