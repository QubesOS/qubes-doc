import json
import sys
import argparse

from pathlib import Path


def load_config(root: Path) -> dict[Path, Path]:
    attachment_path = root / "qubes-doc/attachment/icons"
    json_path = attachment_path.parent / "icons-to-update.json"

    try:
        with open(json_path) as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        print(f"File not found: {json_path.absolute()}")
        sys.exit(1)
    except json.decoder.JSONDecodeError:
        print(f"Wrong JSON format: {json_path.absolute()}")
        sys.exit(2)

    config = {}
    for destination, source in data.items():
        destination_path = attachment_path / destination
        if source:
            source_path = root / source
        else:
            source_path = root / destination

        config[destination_path] = source_path

    return config


def update(destination: str, source: str) -> str:
    """Update destination with source

    Return an error message if appropriate.

    If source doesn't exists, do nothing.
    """
    try:
        with open(source, "rb") as source_file:
            content = source_file.read()
    except FileNotFoundError:
        return f"Source file not found, thus skipped (no {source})"

    destination.parent.mkdir(parents=True, exist_ok=True)
    with open(destination, "wb") as destination_file:
        destination_file.write(content)

    return ""


def main(root: Path | str = "."):
    root_path = Path(root)
    config = load_config(root_path)
    qubes_doc_path = root_path / "qubes-doc"

    print(f"Update {qubes_doc_path}")
    results = {}
    for destination, source in config.items():
        results[destination] = update(destination, source)

    exit_code = 0
    success = 0
    for destination, message in results.items():
        if message:
            exit_code = 1
            print(f"Error with {destination}: {message}")
        else:
            success += 1

    print(
        "{success} file{s} successfully updated".format(
            success=success, s="s" if success > 1 else ""
        )
    )

def main_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root", help="Root dir containing all repos", nargs="?", default="."
    )
    args = parser.parse_args()

    main(args.root)

if __name__ == "__main__":
    main_cli()
