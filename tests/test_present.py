import pytest 
from lib.present import *

def test_present_content_empty():
    gift = Present()
    assert gift.contents is None 

def test_present_wrapping_works():
    gift = Present()
    gift.wrap("Sorpresa")
    assert gift.contents == "Sorpresa"

def test_present_unwraping():
    gift = Present()
    gift.wrap("Something")
    destapado = gift.unwrap()
    assert destapado == "Something"