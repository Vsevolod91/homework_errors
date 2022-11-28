from project.get_val import get_val

def test_get_val():
    assert get_val({"name": "Max"}, "name", "Ivan") == "Max"
    assert get_val({"name": "Max"}, "age") == None
