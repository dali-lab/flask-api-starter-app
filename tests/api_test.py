import pytest
from flask import jsonify


class TestAPI:

    def test_route(self, testapp):
        response = testapp.get('/module/sample')
        response_data = response.json
        assert response_data['id'] == 1
