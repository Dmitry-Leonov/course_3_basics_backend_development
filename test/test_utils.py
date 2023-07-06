from src.utils import sort_by_date


def test_sort_by_date():
    assert sort_by_date([{"ключ1": "значение1"}, {"ключ2": "значение2"}])