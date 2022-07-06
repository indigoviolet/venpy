import pytest
from venpy import none_throws


def test_none_throws():
    assert none_throws(2) == 2
    with pytest.raises(ValueError, match=r"^Unexpected None$"):
        none_throws(None)

    with pytest.raises(ValueError, match="^Did not expect that$"):
        none_throws(None, "Did not expect that")
