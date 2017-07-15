class MyClass(object):
    def __init__(self):
        pass  # some implementation


class DerivedClass1(MyClass):
    def __init__(self):
        # call superclass __init__ (?)
        super(type(self), self).__init__()
        self.x = 1


class DerivedClass2(MyClass):
    def __init__(self):
        # call superclass __init__ (?)
        super(self.__class__, self).__init__()
        self.x = 2
