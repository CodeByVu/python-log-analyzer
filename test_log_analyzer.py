import sys

import pytest

from log_analyzer import get_log_level, keyword_matches, main


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


def test_main_missing_filename(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py'])

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2


def test_main_without_keyword(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'sample.log'
    log_file.write_text('INFO Application started\nERROR Database connection failed')

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file)])

    main()

    captured = capsys.readouterr()
    assert 'No keyword provided. Skipping keyword search.' in captured.out


def test_main_with_keyword(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'sample.log'
    log_file.write_text('INFO Application started\nERROR Database connection failed\nWARNING Database response delayed')

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file), '--keyword', 'DATABASE'])

    main()

    captured = capsys.readouterr()

    assert 'ERROR Database connection failed' in captured.out
    assert 'WARNING Database response delayed' in captured.out
    assert 'KEYWORD MATCHES: 2' in captured.out
