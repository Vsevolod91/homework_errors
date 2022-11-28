from project.set_ import set_

def test_set__for_none_args():
    assert set_({"a": {"b": {"c": 3}}}, [None, None, None], 100) == {"a": {"b": {"c": 3}}, None: {None: {None: 100}}}
    assert set_({"a": {"b": {"c": 3}}}, [None], None) == {"a": {"b": {"c": 3}}, None: None}
