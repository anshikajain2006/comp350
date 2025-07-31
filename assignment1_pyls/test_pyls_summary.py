import os
from pyls_summary import scan_and_group_by_extension


def create_file(path, name, content):
    """Helper to create a file with given content."""
    file_path = path / name
    file_path.write_text(content)
    return file_path


def test_scan_and_group_by_extension(tmp_path):
    create_file(tmp_path, "file1.txt", "hello")             
    create_file(tmp_path, "file2.txt", "world!")            
    create_file(tmp_path, "image.jpg", "jpeg data")         
    create_file(tmp_path, "readme", "no extension")        
    create_file(tmp_path, "data.csv", "1,2,3,4")            


    result = scan_and_group_by_extension(tmp_path)

    # Assertions
    assert result[".txt"]["count"] == 2
    assert result[".txt"]["size"] == 11

    assert result[".jpg"]["count"] == 1
    assert result[".jpg"]["size"] == 9

    assert result[".csv"]["count"] == 1
    assert result[".csv"]["size"] == 7

    assert result[""]["count"] == 1  
    assert result[""]["size"] == 13
