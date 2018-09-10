#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-08-21
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [ocp7](http://github.com/freezed/ocp7/) project.

"""
from flask import Flask, request, render_template
from .classes import Place, Query

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['POST', 'GET'])
def index():
    """ Index View """

    # Default variables
    view_vars = app.config['VIEW_DEFAULT_VARS']

    # Catch posted data from form
    if "submit" in request.form:
        # Parse text input
        query = Query(request.form['textinput'])
        query.parse()

        # Request & filter data
        place = Place(query.in_string)

        # basic server loggin
        log = [
            "input :[{}]".format(request.form['textinput']),
            "string:[{}]".format(query.in_string),
        ]
        place.trigger_api()
        log.append("query :[{}]".format(place.query))

        # Get map URL for address
        if place.geo_data['status']:
            view_vars['map_img_src'] = place.get_map_src()
            view_vars['map_link'] = app.config['APP']['MAP_LINK'].format(**place.geo_data['location'])
            view_vars['text'] = [place.geo_data['formatted_address']]
            log.append("coord :[{}]".format(place.geo_data['location']))

        else:
            # No geo_data : feeds with place.geo_data for loggin
            view_vars['text'].append("Ça me dit rien gamin  …")
            view_vars['map_img_src'] = app.config['VIEW_DEFAULT_VARS']['map_img_src']
            view_vars['map_link'] = app.config['VIEW_DEFAULT_VARS']['map_link']
            log.append("geo_data=#{}#".format(place.geo_data))

        # Get wikimedia data
        if place.article_data['status']:
            view_vars['text'].append(place.article_data['extract'])

        else:
            # No extract : feeds with place.article_data for loggin
            view_vars['text'].append("J'ai la mémoire qui flanche de temps en temps…")
            log.append("article_data=#{}#".format(place.article_data))

        # print server loggin
        for line in log:
            print(line)

    # Return view with vars
    return render_template("index.html", **view_vars)


if __name__ == "__main__":
    app.run()
