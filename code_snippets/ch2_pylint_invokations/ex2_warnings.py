# pylint: disable=R,C
def mutable_default_arg(sequence=[]):
    pass


class Class:
    def __init__(self, x):
        self.x = x


class Subclass(Class):
    def __init__(self, x):
        self.y = x + 1
