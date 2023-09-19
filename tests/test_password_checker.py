import pytest
from lib.password_checker import *

def expect_and_return_error_message(password):
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check(password)
    return str(e.value)

def test_empty_string_is_invalid_password():
    error_message = expect_and_return_error_message("")
    assert error_message == "Invalid password, must be 8+ characters."

def test_7_character_password_is_invalid():
    error_message = expect_and_return_error_message("isogram")
    assert error_message == "Invalid password, must be 8+ characters."

def test_8_character_password_is_valid():
    checker = PasswordChecker()
    assert checker.check("12345678") == True

def test_non_string_type_is_invalid():
    error_message = expect_and_return_error_message(["top", "secret"])
    assert error_message == "Invalid password, must be 8+ characters."

def test_type_without_len_method_raises_type_error():
    checker = PasswordChecker()
    with pytest.raises(TypeError) as e:
        checker.check(0)
    error_message = str(e.value)
    assert error_message == "object of type 'int' has no len()"
