from collections import defaultdict

from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = defaultdict(int)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        correct_ingredients = ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]
        if ingredient_type in correct_ingredients and self.can_add(quantity):
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = 0
            self.ingredients[ingredient_type] += quantity
            # self.capacity -= quantity  # BEWARE OF THIS
        elif not self.can_add(quantity):
            raise ValueError("Not enough space in factory")
        elif ingredient_type not in correct_ingredients:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type not in self.ingredients:
            raise KeyError("No such product in the factory")
        if ingredient_type in self.ingredients and self.ingredients[ingredient_type] >= quantity:
            self.ingredients[ingredient_type] -= quantity
            # self.capacity += quantity  ############
        elif self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")

    def add_recipe(self, recipe_name: str, recipe: dict):
        if recipe_name not in self.recipes:
            self.recipes[recipe_name] = recipe
        else:
            self.recipes[recipe_name].update(recipe)

    def make_chocolate(self, recipe_name: str):
        if recipe_name in self.recipes.keys():
            self.products[recipe_name] += 1
            for pr in self.recipes[recipe_name].keys():
                self.remove_ingredient(pr, quantity=self.recipes[recipe_name][pr])
        if recipe_name not in self.recipes.keys():
            raise TypeError("No such recipe")
