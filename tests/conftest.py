from typing import Any
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from src.DBManager import DBManager


@pytest.fixture
def employer():
    return {
        "id": "123",
        "name": "Test Company",
        "site_url": "https://test.com",
        "area": {"name": "Moscow"}
    }


@pytest.fixture
def vacancies():
    return {
        "items": [
            {"id": "1", "name": "Python dev"},
            {"id": "2", "name": "Backend dev"}
        ],
        "pages": 1
    }


@pytest.fixture
def data():
    return [
        {
            "employers": {
                "id": 1,
                "employer_name": "Test Company",
                "site_url": "https://test.com",
                "city": "Moscow",
            },
            "vacancies": [
                {
                    "id": 101,
                    "name": "Python dev",
                    "salary": {"from": 100000, "to": 150000, "currency": "RUR"},
                    "employer": {"id": 1, "name": "Test Company"},
                    "area": {"name": "Moscow"},
                    "alternate_url": "https://hh.ru/vacancy/101",
                    "published_at": "2024-01-01",
                }
            ],
        }
    ]


@pytest.fixture
def db_manager_with_cursor():
    with patch("src.DBManager.psycopg2.connect") as mock_connect:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_connect.return_value.__enter__.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        manager = DBManager(params={}, database_name="test_db")
        yield manager, mock_cursor
