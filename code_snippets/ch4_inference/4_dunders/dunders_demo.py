class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return A(self.value + other.value)


a1 = A(3)
a2 = A(5)
a3 = a1 + a2
assert a3.value == 8


class CtxMgr:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with CtxMgr() as obj:
    pass
