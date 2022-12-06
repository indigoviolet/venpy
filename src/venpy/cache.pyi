from typing import Callable, TypeVar
from typing_extensions import ParamSpec

T = TypeVar("T")
P = ParamSpec("P")


def cache(wrapped: Callable[P, T]) -> Callable[P, T]:
    ...
