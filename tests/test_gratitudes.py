from lib.gratitudes import *

def test_gratitudes_start_empty():
    my_gratitudes = Gratitudes()
    assert my_gratitudes.gratitudes == []

def test_gratitudes_can_add_gratitude():
    my_gratitudes = Gratitudes()
    my_gratitudes.add("Pair programming")
    assert my_gratitudes.gratitudes == ["Pair programming"]

def test_gratitudes_are_formatted_correctly():
    my_gratitudes = Gratitudes()
    my_gratitudes.add("Apples")
    my_gratitudes.add("Oranges")
    result = my_gratitudes.format()
    assert result == "Be grateful for: Apples, Oranges"