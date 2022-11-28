from project.set_ import set_

def test_set_():
    assert set_({"a": {"b": {"c": 3}}}, ["a", "b", "c"], 4) == {"a": {"b": {"c": 4}}}
    assert set_({"a": {"b": {"c": 3}}}, [1, 2, 3, 4, 5], 100) == {"a": {"b": {"c": 3}}, 1: {2: {3: {4: {5: 100}}}}}

