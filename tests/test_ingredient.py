import pytest
from unittest.mock import patch
from praktikum_code.database import Database
from praktikum_code.ingredient_types import *
from mok_data import RValues


class TestIngredient:
    @patch('praktikum_code.database.Database.available_ingredients', return_value=RValues.MOCK_INGREDIENT_LIST)
    @pytest.mark.parametrize('ingredient_index, expected_ingredient_price', [
        (0, 100),
        (1, 200),
        (2, 300),
        (3, 100),
        (4, 200),
        (5, 300)
    ])
    def test_get_price_matches_index(self, mock_ingredient_list, ingredient_index, expected_ingredient_price):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[ingredient_index].get_price() == expected_ingredient_price

    @patch('praktikum_code.database.Database.available_ingredients', return_value=RValues.MOCK_INGREDIENT_LIST)
    @pytest.mark.parametrize('ingredient_index, expected_ingredient_name', [
        (0, "hot sauce"),
        (1, "sour cream"),
        (2, "chili sauce"),
        (3, "cutlet"),
        (4, "dinosaur"),
        (5, "sausage")
    ])
    def test_get_name_matches_index(self, mock_ingredient_list, ingredient_index, expected_ingredient_name ):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[ingredient_index].get_name() == expected_ingredient_name

    @patch('praktikum_code.database.Database.available_ingredients', return_value=RValues.MOCK_INGREDIENT_LIST)
    @pytest.mark.parametrize('ingredient_index, expected_ingredient_type', [
        (0, INGREDIENT_TYPE_SAUCE),
        (1, INGREDIENT_TYPE_SAUCE),
        (2, INGREDIENT_TYPE_SAUCE),
        (3, INGREDIENT_TYPE_FILLING),
        (4, INGREDIENT_TYPE_FILLING),
        (5, INGREDIENT_TYPE_FILLING)
    ])
    def test_type_matches_index(self, mock_ingredient_list, ingredient_index, expected_ingredient_type):
        database = Database()
        ingredients = database.available_ingredients()

        assert ingredients[ingredient_index].get_type() == expected_ingredient_type
