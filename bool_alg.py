# boolean max defined as +
# boolean min defined as *
# boolean complement defined as ~

class BoolAlg:
    def __init__(self) -> None:
        self.value = 0

    def __init__(self, value) -> None:
        self.value = value

    def __add__(self, other):
        return BoolAlg(max((self.value, other.value)))

    def __mul__(self, other):
        return BoolAlg(min((self.value, other.value)))

    def __eq__(self, other) -> bool:
        return self.value == other.value

    def __invert__(self):
        if self.value == 0:
            return BoolAlg(1)
        return BoolAlg(0)
