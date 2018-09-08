import flasklocal.classes as script
import os
import json
import requests
import pytest

###############
#### PLACE ####
###############

class TestPlace:
    TXTINPUT = "Salut GrandPy! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    PLACE = script.Place(TXTINPUT)

    def test_get_query(self):
        assert self.PLACE.query == self.TXTINPUT

    def test_geo_data_type(self):
        assert isinstance(self.PLACE.geo_data, dict)

    def test_article_data_type(self):
        assert isinstance(self.PLACE.article_data, dict)

    def test_compare(self):
        assert self.PLACE.compare(self.TXTINPUT) == "salut grandpy! est ce que tu connais l adresse d openclassrooms ?"


class RequestsResponse:
    """ Requests.reponse object mock """
    status_code = 200

    def json():
        return [11, 22, 33, 44, 55]

def mock_requests_get(url, payload):
    """ Requests.get() function mock """

    return RequestsResponse

def test_get_json_valid():
    """ Test Place.get_json() with basic manual mock """

    # backup original function
    orginal_function = script.requests.get

    # override function with my mock
    script.requests.get = mock_requests_get

    # Running the tested function, fake params due to the mock
    response = script.Place.get_json("url", "payload")

    # Test
    assert response[2] == 33

    # Rolling bak
    script.requests.get = orginal_function

class RequestsResponseInvalid:
    """ Requests.reponse object mock """
    status_code = 300

    def json():
        return False

def mock_requests_get_invalid(url, payload):
    """ Requests.get() function mock """
    return RequestsResponseInvalid

def test_get_json_invalid(monkeypatch):
    """ Test Place.get_json() with monkeypatch"""
    monkeypatch.setattr('flasklocal.classes.requests.get', mock_requests_get_invalid)
    response = script.Place.get_json("url", "payload")
    assert not response


###############
#### QUERY ####
###############

class TestQuery:
    QUERY = script.Query(
        "Salut GrandPy! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    )

    def test_get_textinput(self):
        assert self.QUERY._textinput_cf == "salut grandpy! est-ce que tu connais l'adresse d'openclassrooms ?"

    def test_textinput_type(self):
        assert isinstance(self.QUERY._textinput_cf, str)

    def test_stop_type(self):
        assert isinstance(self.QUERY.stop, list)

    def test_parser(self):
        self.QUERY.parse()
        assert self.QUERY.in_string == "openclassrooms"
