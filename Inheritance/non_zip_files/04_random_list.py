import random


class RandomList(list):
    def get_random_element(self):
        element_to_go = random.choice(self)
        self.remove(element_to_go)
        return element_to_go
