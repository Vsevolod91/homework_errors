from project.set_ import set_

def test_set__for_empty_args():
    assert set_({"a": {"b": {"c": 3}}}, [], 100) == {"a": {"b": {"c": 3}}}
    assert set_({}, [1, 2, 3, 4], 100) == {1: {2: {3: {4: 100}}}}
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b", "c"], "") == {"a": {"b": {"c": ""}}}
    
