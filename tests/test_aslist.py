from venpy import aslist
import pytest


@aslist
def ints():
    for i in range(3):
        yield i


def test_ints_aslist():
    output = ints()
    assert isinstance(output, list), f"output type is list {output=} {type(output)=}"
    assert output == [0, 1, 2]
