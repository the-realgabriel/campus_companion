import pytest
from src.utils.persistence import save_data, load_data

def test_save_data(tmp_path):
    test_data = {"key": "value"}
    test_file = tmp_path / "test.json"
    
    save_data(test_file, test_data)
    
    with open(test_file, "r") as f:
        loaded_data = json.load(f)
    
    assert loaded_data == test_data

def test_load_data_existing_file(tmp_path):
    test_data = {"key": "value"}
    test_file = tmp_path / "test.json"
    
    with open(test_file, "w") as f:
        json.dump(test_data, f)
    
    loaded_data = load_data(test_file, {})
    
    assert loaded_data == test_data

def test_load_data_non_existing_file(tmp_path):
    test_file = tmp_path / "non_existing.json"
    loaded_data = load_data(test_file, {"default": "value"})
    
    assert loaded_data == {"default": "value"}