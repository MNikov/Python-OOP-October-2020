from project.person import Person


class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


c = Child('asd', 12)
print(c)