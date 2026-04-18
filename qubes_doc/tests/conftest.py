import pytest
from pathlib import Path


@pytest.fixture
def tmp_data(tmp_path) -> Path:
    """Returns a tmp_path populated with fixtures"""
    doc_path = tmp_path / "qubes-doc/attachment/icons"
    fixtures = {
        doc_path / "qubes-core/file-to-keep": "file to keep",
        tmp_path / "qubes-core/file-to-keep": "file to keep",
        doc_path / "qubes-core/subdir/other-name": "file to keep with different name",
        tmp_path
        / "qubes-core/somewhere-else/file-to-rename": "file to keep with different name",
        doc_path / "qubes-artwork/file-to-update": "file to update",
        tmp_path / "qubes-artwork/file-to-update": "file updated",
        tmp_path / "qubes-artwork/file-to-add": "file added",
        doc_path / "qubes-missing-repo/file-to-keep": "another file to keep",
        doc_path.parent / "icons-to-update.json": """
{
    "qubes-core/file-to-keep": "",
    "qubes-core/subdir/other-name": "qubes-core/somewhere-else/file-to-rename",
    "qubes-artwork/file-to-update": "",
    "qubes-artwork/file-to-add": "",
    "qubes-missing-repo/file-to-keep": ""
}
""",
    }

    for path, content in fixtures.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as original_file:
            original_file.write(content)

    return tmp_path
