import pytest
from venpy import keydefaultdict


def test_keydefaultdict_default():
    kd = keydefaultdict[int, int](lambda x: x * 2)
    assert kd[4] == 8
    assert 4 in kd
    assert 8 not in kd


def test_defaultdict_None():
    kd = keydefaultdict[str, str]()
    with pytest.raises(KeyError):
        kd["a"]
