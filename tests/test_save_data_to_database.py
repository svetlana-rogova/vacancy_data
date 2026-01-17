from unittest.mock import MagicMock
from unittest.mock import patch

from src.save_data_to_database import save_data_to_database


def test_save_data_to_database(data):
    fake_data = data
    params = {"user": "test", "password": "test", "host": "localhost"}
    with patch("src.save_data_to_database.psycopg2.connect") as mock_connect:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value = mock_conn
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        save_data_to_database(fake_data, "test_db", params)
        assert mock_connect.called
        assert mock_cursor.execute.call_count == 2
        mock_conn.commit.assert_called_once()
        mock_conn.close.assert_called_once()
