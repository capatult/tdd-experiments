from lib.check_codeword import *

def test_check_codeword_accepts_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_hints_for_close_incorrect_codeword():
    result = check_codeword("hearthstone")
    assert result == "Close, but nope."

def test_check_codeword_rejects_incorrect_codeword():
    result = check_codeword("magic the gathering")
    assert result == "WRONG!"