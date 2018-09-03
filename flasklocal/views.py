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

    # Default response
    query = "… no query …"
    address = "… no address …"
    text = "… no text …"
    map_url = "https://via.placeholder.com/{}x{}?text=no+map".format(*app.config['GOO_API']['MAP_SIZE'])

    # Catch posted data from form
    if "submit" in request.form:
        # Request & filter data
        place = Place(request.form['query'])

        # Get map URL for address
        map_url = place.get_static_map_url()
        query = place.query
        address = place.geo_data['formatted_address']

        # Get wikimedia data
        text = place.article_data['extract']

    # Return view with vars
    return render_template(
        "index.html",
        name=app.config['APP']['NAME'],
        url=app.config['APP']['SRC'],
        query=query,
        address=address,
        text=text,
        map_url=map_url,
    )


if __name__ == "__main__":
    app.run()
