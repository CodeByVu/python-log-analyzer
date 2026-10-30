from log_analyzer import get_log_level, keyword_matches
import pytest


def test_get_log_level():
    result = get_log_level('ERROR Database connection failed') 
    assert result == 'ERROR'

def test_get_log_level_empty_line():
    with pytest.raises(IndexError):
        get_log_level('')

def test_get_log_level_unknown():
    result = get_log_level('In a universe of probabilities, reality is just a choice of observation.')
    assert result == 'In'

def test_keyword_matches_true():
    result = keyword_matches('I love money', 'money')
    assert result == True # result is already a Boolean, so this is often written as: assert result

def test_keyword_matches_false():
    result = keyword_matches('I REALLY love money', 'Bear')
    assert result == False

def test_keyword_matches_lowercase_keyword():
    result = keyword_matches('ERROR Database failed', 'database')
    assert result == True

def test_keyword_matches_uppercase_keyword():
    result = keyword_matches('ERROR Database failed', 'DATABASE')
    assert result == True

def test_keyword_matches_mixedcase_keyword():
    result = keyword_matches('ERROR Database failed', 'dAtaBaSE')
    assert result == True
