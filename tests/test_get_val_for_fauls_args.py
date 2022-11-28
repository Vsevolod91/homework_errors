from project.get_val import get_val

def test_get_val_for_false_args():
    assert get_val({False: "python"}, False) == "python"
    assert get_val({"name": "Max"}, "age", False) == False
