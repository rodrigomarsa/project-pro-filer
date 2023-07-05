from pro_filer.actions.main_actions import show_preview  # NOQA


def test_show_preview_with_files(capsys):
    context = {
        "all_files": [
            "src/1.py",
            "src/2.py",
            "src/u/a.py",
            "src/2.py",
            "src/3.py",
            "src/4.py",
        ],
        "all_dirs": ["src", "src/u"],
    }
    show_preview(context)
    expected = """Found 6 files and 2 directories
First 5 files: ['src/1.py', 'src/2.py', 'src/u/a.py', 'src/2.py', 'src/3.py']
First 5 directories: ['src', 'src/u']\n"""
    captured = capsys.readouterr()
    assert captured.out == expected


def test_show_preview_without_files(capsys):
    context = {"all_files": [], "all_dirs": []}
    show_preview(context)
    expected = "Found 0 files and 0 directories\n"
    captured = capsys.readouterr()
    assert captured.out == expected
