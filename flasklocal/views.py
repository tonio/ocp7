#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Author: freezed <freezed@users.noreply.github.com> 2018-08-21
Version: 0.1
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

This file is part of [ocp7](http://github.com/freezed/ocp7/) project.

"""
from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['POST', 'GET'])
def index():
    response = "…"

    if "submit" in request.form :
            response = request.form['text']

    return render_template(
        "index.html",
        name=app.config['APP']['NAME'],
        url=app.config['APP']['SRC'],
        response=response,
    )

if __name__ == "__main__":
    app.run()
