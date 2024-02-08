"""Class definitions of small objects go here to be imported."""


class Bool0:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("1true")
        return bool(*args)


class Bool1:
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print("2true")
        return bool(*args)