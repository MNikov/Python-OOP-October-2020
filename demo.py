class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def test(self, a, b):
        if a > b:
            return 'q'
        return a - b

t = A(1, 4)
if t.test(1, 4):
    print('asd')