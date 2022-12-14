import math


def test_math_pi():
    assert round(math.pi, 2) == 3.14, 'Тест не пройден'


def test_math_sqrt():
    assert math.sqrt(2) == 2**(0.5), 'Тест не пройден'
    assert math.sqrt(4) == 2, 'Тест не пройден'


def test_math_pow():
    assert math.pow(2, 0.5) == 2 ** 0.5, 'Тест не пройден'
    assert math.pow(2, 3) == 8, 'Тест не пройден'
    assert math.pow(4, -1) == 0.25, 'Тест не пройден'
    assert math.pow(4, -0.5) == 0.5, 'Тест не пройден'


def test_math_hypot():
    assert math.hypot(2, 4) == (2 ** 2 + 4 ** 2) ** 0.5, 'Тест не пройден'
    assert math.hypot(-2, 0) == 2, 'Тест не пройден'
    assert math.hypot(0, 2) == 2, 'Тест не пройден'


def test_sorted():
    assert sorted([4, 3, 2]) == [2, 3, 4], 'Тест не пройден'
    assert sorted([3, 4, 2], reverse=True) == [4, 3, 2], 'Тест не пройден'


def test_map():
    assert list(map(lambda x: x**2, [5, 2, 3])) == [25, 4, 9], 'Тест не пройден'
    assert list(map(int, ['5', '2', '3'])) == [5, 2, 3], 'Тест не пройден'


def test_filter():
    assert list(filter(lambda x: x > 0, [-2, -1, 0, 3, 2])) == [3, 2], 'Тест не пройден'
    assert list(filter(lambda x: -1 < x < 1, [-2, -1, 0, 1, 2])) == [0], 'Тест не пройден'