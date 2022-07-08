from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from typing import Literal

from venpy import ContextMixin


@dataclass
class FakeContextMixin(ContextMixin):
    status: Literal["in", "out", "neither"] = "neither"

    @contextmanager
    def __context__(self):
        self.status = "in"
        yield self
        self.status = "out"


def test_context_mixin():
    with FakeContextMixin() as tc:
        assert tc.status == "in"

    assert tc.status == "out"
