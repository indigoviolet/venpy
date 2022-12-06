from typing import Callable, TypeVar, Any, Generator
from typing_extensions import ParamSpec

T = TypeVar("T")
P = ParamSpec("P")


def aslist(wrapped: Callable[P, Generator[T, Any, Any]]) -> Callable[P, list[T]]:
    ...
