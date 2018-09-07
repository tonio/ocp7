import flasklocal.classes as script
import pytest

###############
#### PLACE ####
###############


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
