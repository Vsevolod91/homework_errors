from project.get_val import get_val

def test_get_val_for_empty_args():
    assert get_val({}, "age", "Ivan") == "Ivan"
    assert get_val({}, "", "Ivan") == "Ivan"
    assert get_val({}, "", "") == ""
