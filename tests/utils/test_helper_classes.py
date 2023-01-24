
import pytest

from utils import helper_classes as hc
from unittest.mock import Mock, patch
from tests import req_patch
import requests

@pytest.fixture
def Randnamegen():
    return hc.RandomNameGenerator("m","NP")


mock_response = req_patch.mock_response
def test_make_api_call(Randnamegen, mock_response):
    assert Randnamegen.make_api_call() == ("Aaditya","SUBEDI")



@pytest.fixture
def mock_get():
    with patch('requests.get') as mocked_get:
        yield mocked_get



def test_request_timeoutError(Randnamegen, mock_get):
    mock_get.side_effect = requests.exceptions.Timeout
    with pytest.raises(hc.APIException):
        Randnamegen.make_api_call()


def test_request_connectionError(Randnamegen, mock_get):
    mock_get.side_effect = requests.exceptions.ConnectionError
    with pytest.raises(hc.APIException):
        Randnamegen.make_api_call()





def test_request_get_reqexception(Randnamegen, mock_get):
    mock_get.side_effect = requests.exceptions.RequestException
    with pytest.raises(hc.APIException):
        Randnamegen.make_api_call()