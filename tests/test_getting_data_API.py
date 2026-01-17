from unittest.mock import Mock
from unittest.mock import patch

from src.getting_data_API import getting_data


def test_getting_data(employer, vacancies):
    with patch("src.getting_data_API.requests.get") as mock_get:
        mock_get.side_effect = [
            Mock(status_code=200, json=lambda: employer),
            Mock(status_code=200, json=lambda: vacancies),
        ]
        result = getting_data(["123"])
    assert isinstance(result, list)
    assert len(result) == 1
    company = result[0]["employers"]
    vacancies = result[0]["vacancies"]
    assert company["employer_name"] == "Test Company"
    assert company["city"] == "Moscow"
    assert len(vacancies) == 2
