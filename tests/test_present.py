import pytest 
from lib.present import *

def test_present_content_empty():
    gift = Present()
    assert gift.contents is None 

def test_present_wrapping_works():
    gift = Present()
    gift.wrap("Sorpresa")
    assert gift.contents == "Sorpresa"

def test_present_unwrapping():
    gift = Present()
    gift.wrap("Something")
    destapado = gift.unwrap()
    assert destapado == "Something"

def test_present_wrapping_raises_error_if_contents_is_none():
    gift = Present()
    gift.wrap("Mystery item")
    with pytest.raises(Exception) as e:
        gift.wrap("Another mystery item")
    error_message = str(e.value)
    assert error_message == "A contents has alredy been wrapped."

def test_present_unwrapping_raises_error_if_contents_is_not_none():
    gift = Present()
    with pytest.raises(Exception) as e:
        gift.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
