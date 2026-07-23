from pathlib import Path
from qubes_doc.update_icons import main


def get_content(tmp_data: Path, sub_path: str):
    full_path = tmp_data / "qubes-doc/attachment/icons" / sub_path
    with open(full_path) as file:
        content = file.read()
    return content


def test_main(tmp_data):
    main(tmp_data)

    assert get_content(tmp_data, "qubes-core/file-to-keep") == "file to keep"
    assert (
        get_content(tmp_data, "qubes-core/subdir/other-name")
        == "file to keep with different name"
    )
    assert get_content(tmp_data, "qubes-artwork/file-to-update") == "file updated"
    assert get_content(tmp_data, "qubes-artwork/file-to-add") == "file added"

    assert (
        get_content(tmp_data, "qubes-missing-repo/file-to-keep")
        == "another file to keep"
    )
