from lib.report_length import *

def test_report_length_reports_length_of_empty_string():
    result = report_length("")
    assert result == "This string was 0 characters long."

def test_report_length_reports_length_of_single_character_string():
    result = report_length("#")
    assert result == "This string was 1 characters long."

def test_report_length_reports_length_of_long_string():
    result = report_length("Abcdefghijklmnopqrstuvwxyz.")
    assert result == "This string was 27 characters long."