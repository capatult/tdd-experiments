from lib.string_builder import *

def test_string_builder_starts_empty():
    string_builder = StringBuilder()
    assert string_builder.str == ""

def test_string_builder_can_add_string():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    assert string_builder.str == "Hello"
    assert string_builder.size() == 5

def test_string_builder_can_add_multiple_strings():
    string_builder = StringBuilder()
    string_builder.add("Hello")
    string_builder.add(", ")
    string_builder.add("World!")
    assert string_builder.str == "Hello, World!"
    assert string_builder.size() == 13

def test_string_builder_can_output():
    string_builder = StringBuilder()
    string_builder.add("Goodbye")
    assert string_builder.output() == "Goodbye"