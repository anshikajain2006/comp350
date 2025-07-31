import os
from collections import defaultdict

def scan_and_group_by_extension(path):
    """
    Scans the directory at `path` and returns a dictionary with:
    - keys as file extensions (e.g., '.txt', '')
    - values as dicts with:
        - 'count': number of files with that extension
        - 'size': total size in bytes of those files
    """
    result = defaultdict(lambda: {'count': 0, 'size': 0})

    for entry in os.scandir(path):
        if entry.is_file():
            ext = os.path.splitext(entry.name)[1]  # includes dot, or ''
            size = entry.stat().st_size

            result[ext]['count'] += 1
            result[ext]['size'] += size

    return result


def print_summary(ext_data):
    """
    Given a dict of extension → {count, size}, print the summary.
    """
    for ext, stats in ext_data.items():
        ext_label = ext if ext else "(no extension)"
        print(f"{ext_label}: {stats['count']} file(s), {stats['size']} bytes")


def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python pyls_summary.py <directory>")
        return

    path = sys.argv[1]
    if not os.path.isdir(path):
        print(f"Error: {path} is not a directory.")
        return

    ext_data = scan_and_group_by_extension(path)
    print_summary(ext_data)


if __name__ == "__main__":
    main()
