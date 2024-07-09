from unittest.mock import Mock, patch
from praktikum_code.database import Database
from praktikum_code.burger import Burger
from praktikum_code.ingredient_types import *
from mok_data import RValues


class TestBurger:
    @patch('praktikum_code.database.Database.available_buns', return_value=RValues.MOCK_BUNS_LIST)
    def test_set_buns_matches_index(self, mock_available_buns):
        database = Database()
        buns = database.available_buns()
        burger = Burger()
        burger.set_buns(buns[0])

        assert burger.bun == buns[0]

    @patch('praktikum_code.database.Database.available_ingredients', return_value=RValues.MOCK_INGREDIENT_LIST)
    def test_add_ingredient_list_contains_matched_indexes(self, mock_ingredient_list):
        database = Database()
        ingredients = database.available_ingredients()
        burger = Burger()
        burger.add_ingredient(ingredients[0])
        burger.add_ingredient(ingredients[5])

        assert burger.ingredients == [ingredients[0], ingredients[5]]

    def test_remove_ingredient_list_is_empty(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient_two_objects_swap_indexes(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_2 and burger.ingredients[1] == mock_ingredient_1

    def test_get_price_got_expected_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 100
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        actual_price = burger.get_price()
        expected_price = 100*2 + 100

        assert actual_price == expected_price

    def test_get_receipt_got_expected_receipt(self):
        mock_bun = Mock()
        mock_bun.get_name.return_value = "black bun"
        mock_bun.get_price.return_value = 100
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_name.return_value = "cutlet"
        mock_ingredient.get_price.return_value = 100
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        actual_receipt = burger.get_receipt()
        expected_receipt = (
            "(==== black bun ====)\n"
            "= filling cutlet =\n"
            "(==== black bun ====)\n"
            "\n"
            "Price: 300"
        )

        assert actual_receipt == expected_receipt
