from lib.counter import *

def test_counter_class_begins_with_count_of_zero():
    my_counter = Counter()
    assert my_counter.report() == "Counted to 0 so far."

def test_counter_class_add_method_works():
    my_counter = Counter()
    my_counter.add(42)
    assert my_counter.report() == "Counted to 42 so far."

def test_counter_class_repeated_adding():
    my_counter = Counter()
    my_counter.add(5)
    my_counter.add(10)
    my_counter.add(-2)
    assert my_counter.report() == "Counted to 13 so far."
