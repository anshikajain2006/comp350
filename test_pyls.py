import io
import sys
import pytest
from pyls import pyls

@pytest.fixture
def capture():
    oldstdout = sys.stdout
    sio = io.StringIO()
    sys.stdout = sio
    yield sio  
    sys.stdout = oldstdout

def test_dummy():
    assert 2 == 2, "Two and two must be the same"

# def test_dummy_fails():
#     assert 2 == 3, "Two and three must be the same (Really?)"

def test_pyls_output(capture):
    pyls(".")
    output = capture.getvalue()
    assert "test_pyls.py" in output or "pyls.py" in output, "Should list this file or main file"
