from bubble_sort import bubble_sort

def test_tiny_list():
    list = [6, 7, 8, 9]

    result = bubble_sort(list)

    assert result == [6, 7, 8, 9]

def test_large_list():
    number = list(range(143, 0, -1))
    result = bubble_sort(number)

    assert result == list(range(1, 144))

def test_empty_list():
    assert bubble_sort([]) == []

import pytest
def test_not_a_list():
    with pytest.raises(TypeError):
        bubble_sort(123)