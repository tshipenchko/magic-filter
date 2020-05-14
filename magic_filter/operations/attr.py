from typing import Any, Callable, List

from ..attribute import Attribute
from .simple import SimpleOperation


class AttrOperation(SimpleOperation):
    def __init__(self, operation: Callable[..., bool], value: Any, chain: List[Attribute]) -> None:
        super().__init__(value=value, chain=chain)
        self.operation = operation

    def resolve(self, value: Any) -> bool:
        return self.operation(value, self.value)

    __slots__ = ("operation", "value", "_chain")
