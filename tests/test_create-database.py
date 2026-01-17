from unittest.mock import MagicMock
from unittest.mock import patch

from src.create_database import create_database


@patch("src.create_database.psycopg2.connect")
def test_create_database(mock_connect):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn
    create_database("test_db", {"user": "test", "password": "123"})
    assert mock_connect.called
    executed_queries = [call.args[0] for call in mock_cursor.execute.call_args_list]
    assert "DROP DATABASE IF EXISTS test_db" in executed_queries
    assert "CREATE DATABASE test_db" in executed_queries
