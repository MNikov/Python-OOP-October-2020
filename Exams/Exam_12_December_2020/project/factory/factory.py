from abc import ABC, abstractmethod


class Factory(ABC):
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.ingredients = {}

    @abstractmethod
    def add_ingredient(self, ingredient_type: str, quantity: int):
        pass

    @abstractmethod
    def remove_ingredient(self, ingredient_type: str, quantity: int):
        pass

    def can_add(self, value: int):
        capacity_taken = sum([v for k, v in self.ingredients.items()])
        return self.capacity >= capacity_taken + value
