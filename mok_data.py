from praktikum_code.bun import Bun
from praktikum_code.ingredient import Ingredient
from praktikum_code.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class RValues:
    MOCK_BUNS_LIST = [Bun("black bun", 100), Bun("white bun", 200),
                      Bun("red bun", 300)]

    MOCK_INGREDIENT_LIST = [Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                            Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                            Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                            Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                            Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                            Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)]

