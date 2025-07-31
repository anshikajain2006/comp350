import pytest
import tempfile
from pathlib import Path
from pyls import pyls


@pytest.fixture
def sample_dir():
    """Create a temporary directory with sample files of different sizes."""
    with tempfile.TemporaryDirectory() as tmpdirname:
        dir_path = Path(tmpdirname)

        # Create sample files and directories
        (dir_path / "small.txt").write_text("hello")               
        (dir_path / "medium.txt").write_text("hello world")       
        (dir_path / "large.txt").write_text("a" * 1000)           
        (dir_path / "subdir").mkdir()                              

        yield dir_path


def test_sort_by_size(capsys, sample_dir):
    """Check that files are sorted in descending order of size when -S is used."""
    pyls(str(sample_dir), longform=False, formatted=False, sort_by_size=True)
    output = capsys.readouterr().out.strip().split('\n')

    expected_order = ["large.txt", "medium.txt", "small.txt", "subdir"]
    output_names = [line.strip().split()[-1].replace('/', '') for line in output]

    # 'subdir' has size 0 so should be last
    assert output_names == expected_order


def test_longform_output(capsys, sample_dir):
    """Check that longform output includes timestamp and size."""
    pyls(str(sample_dir), longform=True, formatted=False, sort_by_size=True)
    output = capsys.readouterr().out.strip().split('\n')

    for line in output:
        parts = line.split()
        assert len(parts) >= 3  
        assert parts[0].count('-') == 2  


def test_formatted_output(capsys, sample_dir):
    """Check that directory names get a trailing slash when -F is used."""
    pyls(str(sample_dir), longform=False, formatted=True, sort_by_size=False)
    output = capsys.readouterr().out.strip().split('\n')

    has_slash = any(line.endswith("subdir/") for line in output)
    assert has_slash


def test_combined_options(capsys, sample_dir):
    """Check that all options work together."""
    pyls(str(sample_dir), longform=True, formatted=True, sort_by_size=True)
    output = capsys.readouterr().out.strip().split('\n')

    found = False
    for line in output:
        parts = line.split()
        if len(parts) >= 3 and parts[-1].endswith("/"):
            found = True
            break
    assert found
