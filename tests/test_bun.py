import pytest
from unittest.mock import patch
from praktikum_code.database import Database
from mok_data import RValues


class TestBun:
    @patch('praktikum_code.database.Database.available_buns', return_value=RValues.MOCK_BUNS_LIST)
    @pytest.mark.parametrize('bun_index, expected_bun_name', [
        (0, 'black bun'),
        (1, 'white bun'),
        (2, 'red bun')
    ])
    def test_get_name_matches_index(self, mock_available_buns, bun_index, expected_bun_name):
        database = Database()
        buns = database.available_buns()

        assert buns[bun_index].get_name() == expected_bun_name

    @patch('praktikum_code.database.Database.available_buns', return_value=RValues.MOCK_BUNS_LIST)
    @pytest.mark.parametrize('bun_index, expected_bun_price', [
        (0, 100),
        (1, 200),
        (2, 300)
    ])
    def test_get_price_matches_index(self, mock_available_buns, bun_index, expected_bun_price):
        database = Database()
        buns = database.available_buns()

        assert buns[bun_index].get_price() == expected_bun_price
