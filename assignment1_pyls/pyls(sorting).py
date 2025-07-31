
"""pyls – a tiny re‑implementation of the Unix `ls` command.

This module can be run as a script or imported and the `pyls` function
called directly from other Python code.
"""

from __future__ import annotations

import argparse
import time
from pathlib import Path

__all__ = [
    "pyls",
]

def pyls(dirname: str = ".", longform: bool = False, formatted: bool = False, sort_by_size: bool = False) -> None:
    """List the contents of *dirname* to **stdout**.

    str bool bool bool -> None

    Parameters
    ----------
    dirname : str, optional
        Path of the directory whose contents will be listed. The default is the
        current directory ``"."``.
    longform : bool, optional
        When *True* each entry is prefixed with its last‑modified timestamp
        (YYYY‑MM‑DD HH:MM) and size in bytes. Defaults to *False*.
    formatted : bool, optional
        When *True* a trailing slash ``/`` is appended to directory names so
        you can visually distinguish them from regular files. Defaults to *False*.
    sort_by_size : bool, optional
        When *True* list is sorted by file size in descending order. Defaults to *False*.

    Example Uses
    ------------
    >>> pyls()                       # plain listing of current dir
    >>> pyls(longform=True)          # long listing
    >>> pyls("/tmp", formatted=True)  # mark directories in /tmp
    >>> pyls(sort_by_size=True)      # sort by file size
    """

    try:
        entries = list(Path(dirname).iterdir())
    except FileNotFoundError:
        print(f"pyls: cannot access '{dirname}': No such directory")
        return

    if sort_by_size:
        entries.sort(key=lambda p: p.stat().st_size, reverse=True)
    else:
        entries.sort(key=lambda p: p.name.lower())

    for entry in entries:
        fields: list[str] = []

        if longform:
            stat = entry.stat()
            timestamp = time.strftime("%Y-%m-%d %H:%M", time.localtime(stat.st_mtime))
            fields.append(timestamp)
            fields.append(f"{stat.st_size:>8}")  # right‑aligned size

        name = entry.name + ("/" if formatted and entry.is_dir() else "")
        fields.append(name)

        print(" ".join(fields))


def _build_cli() -> argparse.ArgumentParser:
    """Return a configured :pyclass:`argparse.ArgumentParser`."""
    parser = argparse.ArgumentParser(
        prog="pyls", description="A baby version of ls implemented in Python."
    )
    parser.add_argument(
        "dirname",
        nargs="?",
        default=".",
        help="Directory whose contents are to be listed (default: current directory).",
    )
    parser.add_argument(
        "-l",
        "--longform",
        action="store_true",
        help="Show <timestamp> <filesize> before each name.",
    )
    parser.add_argument(
        "-F",
        "--formatted",
        action="store_true",
        help="Append '/' after directory names.",
    )
    parser.add_argument(
        "-S",
        "--sort-size",
        action="store_true",
        help="Sort entries by file size in descending order.",
    )
    return parser


def main() -> None:  
    """CLI entry‑point. Parse args and delegate work to :pyfunc:`pyls`."""
    parser = _build_cli()
    args = parser.parse_args()
    pyls(args.dirname, args.longform, args.formatted, args.sort_size)


if __name__ == "__main__":
    main()
