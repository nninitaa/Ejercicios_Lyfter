from function_one import sum_list

def test_list():
    assert sum_list([]) == 0

from function_two import reverse_string

def test_reverse_string():
    assert reverse_string("Hello") == "olleH"

from function_three import sort_words

def test_sort_words():
    assert sort_words("") == ""
