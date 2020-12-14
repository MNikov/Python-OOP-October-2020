from project.factory.factory import Factory


class PaintFactory(Factory):
    def __init__(self, name: str, capacity: int):
        super().__init__(name, capacity)

    def add_ingredient(self, ingredient_type: str, quantity: int):
        correct_ingredients = ["white", "yellow", "blue", "green", "red"]
        if ingredient_type not in correct_ingredients:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")
        if ingredient_type in correct_ingredients and self.can_add(quantity):
            if ingredient_type not in self.ingredients:
                self.ingredients[ingredient_type] = 0
            self.ingredients[ingredient_type] += quantity
            # self.capacity -= quantity  # BEWARE OF THIS
        elif not self.can_add(quantity):
            raise ValueError("Not enough space in factory")


    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients and self.ingredients[ingredient_type] >= quantity:
            self.ingredients[ingredient_type] -= quantity
            # self.capacity += quantity  ############
        if self.ingredients[ingredient_type] < quantity:
            raise ValueError("Ingredient quantity cannot be less than zero")
        elif ingredient_type not in self.ingredients:
            raise KeyError("No such ingredient in the factory")

    @property
    def products(self):
        return self.ingredients
