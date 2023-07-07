from pro_filer.actions.main_actions import find_duplicate_files  # NOQA
import pytest


def test_find_duplicate_files_equals(tmp_path):
    mock_dir = tmp_path / 'pasta'
    mock_dir.mkdir()
    mock_txt_1 = mock_dir / "fake1.txt"
    mock_txt_1.touch()
    mock_txt_1.write_text("oi")
    mock_txt_2 = mock_dir / "fake1.txt"
    mock_txt_2.touch()
    mock_txt_2.write_text("oi")
    context = {"all_files": [str(mock_txt_1), str(mock_txt_2)]}

    captured = find_duplicate_files(context)

    expected = [(str(mock_txt_1), str(mock_txt_2))]

    assert captured == expected


def test_find_duplicate_files_different(tmp_path):
    mock_dir = tmp_path / 'pasta'
    mock_dir.mkdir()
    mock_txt_1 = mock_dir / "fake1.txt"
    mock_txt_1.touch()
    mock_txt_1.write_text("oi")
    mock_txt_2 = mock_dir / "fake2.txt"
    mock_txt_2.touch()
    mock_txt_2.write_text("olá")
    context = {"all_files": [str(mock_txt_1), str(mock_txt_2)]}

    captured = find_duplicate_files(context)

    expected = []

    assert captured == expected


def test_find_duplicate_files_fails():
    with pytest.raises(ValueError, match="All files must exist"):
        context = {"all_files": ["fake1.txt", "fake2.txt"]}
        find_duplicate_files(context)
