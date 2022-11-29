from myfunctions import my_filter
def test_my_filter():
    assert my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5], 'Тест не пройден'