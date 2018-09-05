#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-08-21
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [ocp7](http://github.com/freezed/ocp7/) project.

"""
from flask import Flask, request, render_template
from .classes import Place

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['POST', 'GET'])
def index():
    """ Index View """

    # Default variables
    view_vars = app.config['VIEW_DEFAULT_VARS']

    # Catch posted data from form
    if "submit" in request.form:
        # Request & filter data
        place = Place(request.form['query'])

        # Get map URL for address
        view_vars['map_url'] = place.get_static_map_url()
        view_vars['query'] = place.query
        view_vars['address'] = place.geo_data['formatted_address']

        # Get wikimedia data
        view_vars['text'] = place.article_data['extract']

    # Return view with vars
    return render_template("index.html", **view_vars)


if __name__ == "__main__":
    app.run()
