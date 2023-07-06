from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path


def test_show_disk_usage(tmp_path, capsys):
    content = "content"
    mock_txt = tmp_path / "fake.txt"
    mock_txt.touch()
    mock_txt.write_text(content)
    mock_json = tmp_path / "fake.json"
    mock_json.touch()
    context = {"all_files": [str(mock_txt), str(mock_json)]}

    show_disk_usage(context)
    captured = capsys.readouterr()
    output_txt = f"'{_get_printable_file_path(str(mock_txt))}':".ljust(70)
    output_json = f"'{_get_printable_file_path(str(mock_json))}':".ljust(70)

    expected = f"""{output_txt} 7 (100%)
{output_json} 0 (0%)
Total size: 7\n"""

    assert captured.out == expected
