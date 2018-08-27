#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-08-21
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [ocp7](http://github.com/freezed/ocp7/) project.

"""
import pprint
from flask import Flask, request, render_template
from apicall import goo_geocode, goo_static, filter_api_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['POST', 'GET'])
def index():
    """ Index View """

    # Default response
    filtered_data_formated = "… empty response …"
    map_url = "https://via.placeholder.com/600x300?text=no+map"

    # Catch posted data from form
    if "submit" in request.form:
        query_string = str(request.form['query'])

        # Request & filter data
        filtered_data = filter_api_response(goo_geocode(query_string))

        # Get map URL for address
        map_url = goo_static(filtered_data['formatted_address'])

        filtered_data_formated = pprint.pformat(filtered_data)

    # Redern view with vars
    return render_template(
        "index.html",
        name=app.config['APP']['NAME'],
        url=app.config['APP']['SRC'],
        raw_response=filtered_data_formated,
        map_url=map_url,
    )


if __name__ == "__main__":
    app.run()
