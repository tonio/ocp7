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
        view_vars['dev_log'] = query.parse()

        # Request & filter data
        place = Place(query.in_string)

        # Get map URL for address
        view_vars['map_img_src'] = place.get_map_src()
        view_vars['map_link'] = app.config['APP']['MAP_LINK'].format(**place.geo_data['location'])

        # Dev logging
        view_vars['dev_log'] += "\nquery : «{}»".format(place.query)
        view_vars['dev_log'] += "\naddress : «{}»".format(place.geo_data['formatted_address'])
        view_vars['dev_log'] += "\ncoord : «{}»".format(place.geo_data['location'])

        # Get wikimedia data
        if place.article_data['status']:
            view_vars['text'] = place.article_data['extract']

        else:
            # No extract : feeds with place.article_data for loggin
            view_vars['text'] = place.article_data

    # Return view with vars
    return render_template("index.html", **view_vars)


if __name__ == "__main__":
    app.run()
