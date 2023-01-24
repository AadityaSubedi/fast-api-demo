from main import app
import json
import pytest
import requests
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch
from . import req_patch

payload = {"api_key": "123qwe",
           "endpoint": "generate",
           "gender": "m",
           "country_code": "US",
           }


@pytest.fixture
def client():
    return TestClient(app)

mock_response = req_patch.mock_response
def test_generate_name(client, mock_response):
    response = client.get('/generate', params=payload)
    assert response.status_code == 200

    data = response.json()["data"]

    assert data['first_name'] == 'Aaditya' and data['last_name'] == 'SUBEDI'
