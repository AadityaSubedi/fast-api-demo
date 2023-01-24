import pytest
from unittest.mock import Mock, patch

mock_data = {
    "results": 1,
    "error": None,
    "data": [
        {
            "salutation": {
                "salutation": "Mr.",
                "initials": "A.",
                "lastname": "SUBEDI"
            },
            "title": None,
            "name": {
                "nickname": None,
                "firstname": {
                    "name": "Aaditya",
                    "name_ascii": "aaditya",
                    "validated": True,
                    "gender": "m",
                    "gender_formatted": "male",
                    "unisex": True,
                    "gender_deviation": 0,
                    "country_code": "US",
                    "country_certainty": 100,
                    "country_rank": 2228,
                    "country_frequency": 79,
                    "alternative_countries": {
                        "NL": 25,
                        "BR": 10,
                        "PT": 8
                    }
                },
                "middlenames": None,
                "lastname": {
                    "name": "SUBEDI",
                    "name_ascii": "subedi",
                    "validated": True,
                    "country_code": "US",
                    "country_certainty": 100,
                    "country_rank": 1390,
                    "country_frequency": 427,
                    "alternative_countries": {
                        "CA": 9,
                        "GB": 6,
                        "PH": 3
                    },
                    "lastnames": [

                    ]
                }
            },
            "email": "subediaaditya007@gmail.com",
            "country": {
                "country_code": "US",
                "country_certainty": 100,
                "country_code_alpha": "USA",
                "name": "United States",
                "continent": "North America",
                "demonym": "American",
                "primary_language_code": "en",
                "primary_language": "English",
                "currency": "USD",
                "alternative_countries": [

                ]
            }
        }
    ]
}


@pytest.fixture
def mock_response():
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response
        yield mock_response



