import sys

import pytest

from log_analyzer import get_log_level, keyword_matches, main


def test_get_log_level():
    result = get_log_level('ERROR Database connection failed') 
    assert result == 'ERROR'


def test_get_log_level_empty_line():
    with pytest.raises(IndexError):
        get_log_level('')


def test_get_log_level_returns_first_word():
    result = get_log_level('NOTICE Cache refresh completed')
    assert result == 'NOTICE'


def test_keyword_matches_true():
    result = keyword_matches('I love money', 'money')
    assert result # result is already a Boolean, so this is often written as: assert result


def test_keyword_matches_false():
    result = keyword_matches('I REALLY love money', 'Bear')
    assert not result


def test_keyword_matches_lowercase_keyword():
    result = keyword_matches('ERROR Database failed', 'database')
    assert result


def test_keyword_matches_uppercase_keyword():
    result = keyword_matches('ERROR Database failed', 'DATABASE')
    assert result


def test_keyword_matches_mixedcase_keyword():
    result = keyword_matches('ERROR Database failed', 'dAtaBaSE')
    assert result


def test_main_missing_filename(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py'])

    with pytest.raises(SystemExit) as exc_info:
        main()
    assert exc_info.value.code == 2


def test_main_file_not_found(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'missing.log'

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file)])

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1

    captured = capsys.readouterr()
    assert 'File not found' in captured.out


def test_main_without_filters(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'sample.log'
    log_file.write_text(
        'INFO Application started\n'
        'ERROR Database connection failed'
    )

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file)])

    main()

    captured = capsys.readouterr()
    assert 'No keyword provided. Skipping keyword search.' in captured.out
    assert 'MATCHES: 0' in captured.out
    assert 'TOTAL: 2' in captured.out

    assert 'INFO Application started' not in captured.out
    assert 'ERROR Database connection failed' not in captured.out


def test_main_with_keyword(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'sample.log'
    log_file.write_text(
        'INFO Application started\n'
        'ERROR Database connection failed\n'
        'WARNING Database response delayed'
    )

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file), '--keyword', 'DATABASE'])

    main()

    captured = capsys.readouterr()

    assert 'ERROR Database connection failed' in captured.out
    assert 'WARNING Database response delayed' in captured.out
    assert 'MATCHES: 2' in captured.out
    assert 'TOTAL: 3' in captured.out

    assert 'INFO Application started' not in captured.out


def test_main_critical_log_level(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'sample.log'
    log_file.write_text(
        'CRITICAL System failure\n'
        'INFO Application stopped'
    )

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file)])

    main()

    captured = capsys.readouterr()

    assert 'CRITICAL: 1' in captured.out
    assert 'INFO: 1' in captured.out
    assert 'TOTAL: 2' in captured.out
    assert 'CRITICAL PCT: 50.0%' in captured.out


def test_main_invalid_log_level(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', 'sample.log', '--level', 'PEAR'])

    with pytest.raises(SystemExit) as err_code:
        main()

    assert err_code.value.code == 2


def test_main_with_level_filter(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'sample.log'
    log_file.write_text(
        'INFO Application started\n'
        'ERROR Database connection failed\n'
        'WARNING Database response delayed\n'
        'CRITICAL System failure\n'
        'DEBUG Detailed diagnostic information'
    )

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file), '--level', 'ERROR'])

    main()

    captured = capsys.readouterr()

    assert 'ERROR: 1' in captured.out
    assert 'MATCHES: 1' in captured.out
    assert 'ERROR Database connection failed' in captured.out
    assert 'INFO: 1' in captured.out
    assert 'WARNING: 1' in captured.out
    assert 'CRITICAL: 1' in captured.out
    assert 'DEBUG: 1' in captured.out
    assert 'UNKNOWN: 0' in captured.out
    assert 'TOTAL: 5' in captured.out

    assert 'INFO Application started' not in captured.out
    assert 'WARNING Database response delayed' not in captured.out
    assert 'CRITICAL System failure' not in captured.out
    assert 'DEBUG Detailed diagnostic information' not in captured.out


def test_main_level_filter_case_insensitive(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'sample.log'
    log_file.write_text(
        'INFO Application started\n'
        'ERROR Database connection failed\n'
        'WARNING Database response delayed'
    )

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file), '--level', 'ErROr'])

    main()

    captured = capsys.readouterr()

    assert 'ERROR: 1' in captured.out
    assert 'MATCHES: 1' in captured.out
    assert 'ERROR Database connection failed' in captured.out
    assert 'TOTAL: 3' in captured.out

    assert 'INFO Application started' not in captured.out
    assert 'WARNING Database response delayed' not in captured.out


def test_main_unknown_level_filter(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'sample.log'
    log_file.write_text(
        'INFO Application started\n'
        'NOTICE Cache refresh completed\n'
        'ERROR Database connection failed\n'
        'TRACE Detailed trace entry'
    )

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file), '--level', 'UNKNOWN'])

    main()

    captured = capsys.readouterr()

    assert 'UNKNOWN: 2' in captured.out
    assert 'MATCHES: 2' in captured.out
    assert 'NOTICE Cache refresh completed' in captured.out
    assert 'TRACE Detailed trace entry' in captured.out
    assert 'INFO: 1' in captured.out
    assert 'ERROR: 1' in captured.out
    assert 'TOTAL: 4' in captured.out

    assert 'INFO Application started' not in captured.out
    assert 'ERROR Database connection failed' not in captured.out


def test_main_combined_filters(monkeypatch, tmp_path, capsys):
    log_file = tmp_path / 'sample.log'
    log_file.write_text(
        'INFO Application started\n'
        'ERROR Database connection failed\n'
        'WARNING Database response delayed\n'
        'ERROR Authentication failed\n'
        'CRITICAL Database process failed'
    )

    monkeypatch.setattr(sys, 'argv', ['log_analyzer.py', str(log_file), '--keyword', 'DATABASE', '--level', 'ERROR'])

    main()

    captured = capsys.readouterr()

    assert 'ERROR Database connection failed' in captured.out
    assert 'MATCHES: 1' in captured.out
    assert 'INFO: 1' in captured.out
    assert 'WARNING: 1' in captured.out
    assert 'ERROR: 2' in captured.out
    assert 'CRITICAL: 1' in captured.out
    assert 'DEBUG: 0' in captured.out
    assert 'UNKNOWN: 0' in captured.out
    assert 'TOTAL: 5' in captured.out

    assert 'INFO Application started' not in captured.out
    assert 'WARNING Database response delayed' not in captured.out
    assert 'ERROR Authentication failed' not in captured.out
    assert 'CRITICAL Database process failed' not in captured.out
