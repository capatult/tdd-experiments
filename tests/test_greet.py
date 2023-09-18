from lib.greet import *

def test_greet_returns_desired_greeting():
    result = greet("valued customer")
    assert result == "Hello, valued customer!"