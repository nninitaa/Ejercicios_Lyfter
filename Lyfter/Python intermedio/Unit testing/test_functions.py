from function_one import sum_list

def test_list():
    assert sum_list([]) == 0

def test_number():
    assert sum_list([9]) == 9

def test_normal_list():
    assert sum_list([2, 4, 6, 8]) == 20

from function_two import reverse_string

def test_reverse_string():
    assert reverse_string("Hello") == "olleH"

def test_empty_string():
    assert reverse_string("") == ""

def test_one_letter():
    assert reverse_string("I") == "I"

from function_three import sort_words

def test_sort_words():
    assert sort_words("") == ""

def test_order_words():
    assert sort_words("Hello") == "Hello"

def test_disordered_words():
    assert sort_words("One-One-Two") == "One-One-Two"
