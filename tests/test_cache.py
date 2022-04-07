from venpy import cache


import pytest
from pytest_mock import MockFixture


def impl(x, bar, baz):
    return (x, bar, baz)


@cache
def memoized_function(x, bar, baz):
    return impl(x, bar=bar, baz=baz)


class Memo:
    @cache
    @classmethod
    def memoized_clsmethod(cls, x, bar, baz):
        return impl(x, bar=bar, baz=baz)

    @cache
    def memoized_instmethod(self, x, bar, baz):
        return impl(x, bar=bar, baz=baz)


@pytest.mark.parametrize(
    "f", [memoized_function, Memo.memoized_clsmethod, Memo().memoized_instmethod]
)
def test_is_memoized(f, mocker: MockFixture):
    # init cache
    assert f(1, bar=2, baz=3) == (1, 2, 3)

    # mock and see if it returns the correct result, but was not called for same
    # args/kwargs
    impl_mock = mocker.patch(f"{__name__}.impl")
    assert f(1, bar=2, baz=3) == (1, 2, 3)
    assert impl_mock.mock_calls == []

    # see that it is called for different args/kwargs
    f(3, bar=2, baz=1)
    assert impl_mock.mock_calls == [mocker.call(3, bar=2, baz=1)]


@pytest.mark.parametrize(
    "f", [memoized_function, Memo.memoized_clsmethod, Memo().memoized_instmethod]
)
def test_is_robust_to_args(f, mocker: MockFixture):
    # init cache
    assert f(1, bar=2, baz=3) == (1, 2, 3)

    # mock and see if it returns the correct result, but was not called for same
    # args/kwargs
    impl_mock = mocker.patch(f"{__name__}.impl")
    assert f(baz=3, bar=2, x=1) == (1, 2, 3)
    assert f(1, 2, baz=3) == (1, 2, 3)
    assert impl_mock.mock_calls == []
