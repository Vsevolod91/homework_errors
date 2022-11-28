from project.set_ import set_

def test_set__for_similat_path():
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b", "c", "d", "e"], 100) == {"a": {"b": {"c": {"d" : {"e": 100}}}}}
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b"], 100) == {"a": {"b":100}}
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b"], 100) == {"a": {"b":100}}
    assert set_({"a": {"b": {"c": 3}}}, ["a"], 100) == {"a": 100}

