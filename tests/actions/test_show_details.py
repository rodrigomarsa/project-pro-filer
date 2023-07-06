from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date


def test_show_details_with_existing_file(tmp_path, capsys):
    mock_json = tmp_path / "fake.json"
    mock_json.touch()
    context = {"base_path": str(mock_json)}

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        f"""File name: fake.json
File size in bytes: 0
File type: file
File extension: .json
Last modified date: {date.today()}\n"""
    )


def test_show_details_with_file_without_extension(tmp_path, capsys):
    mock_json = tmp_path / "fake"
    mock_json.touch()
    context = {"base_path": str(mock_json)}

    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == (
        f"""File name: fake
File size in bytes: 0
File type: file
File extension: [no extension]
Last modified date: {date.today()}\n"""
    )


def test_show_details_with_not_existing_file(capsys):
    context = {"base_path": "/home/trybe/????"}
    show_details(context)
    captured = capsys.readouterr()
    assert captured.out == "File '????' does not exist\n"
