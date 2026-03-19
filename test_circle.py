from circle import Circle
import math

def test_perimeter():
    c = Circle(2)
    assert math.isclose(c.perimeter(), 2 * math.pi * 2)


def test_area():
    c = Circle(2)
    assert math.isclose(c.area(), math.pi * (2 ** 2))