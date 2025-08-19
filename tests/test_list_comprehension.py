import pytest
from lib.list_comprehension import return_evens, make_exclamation

def test_return_evens_basic():
    assert return_evens([0, 1, 3, 5, 7, 8, 9]) == [0, 8]

def test_return_evens_empty():
    assert return_evens([1, 3, 5]) == []

def test_make_exclamation_basic():
    assert make_exclamation(["Hello", "I'm doing great", "Python is fun"]) == [
        "Hello!",
        "I'm doing great!",
        "Python is fun!"
    ]

def test_make_exclamation_empty():
    assert make_exclamation([]) == []
