from abc import ABC, abstractmethod
from typing import Any


class BaseOperation(ABC):
    def __init__(self, value: Any) -> None:
        self.value = value

    def __invert__(self) -> "NotOperation":
        return NotOperation(value=self)

    def __and__(self, other: "BaseOperation") -> "AndOperation":
        return AndOperation(value=self, other_value=other)

    def __or__(self, other: "BaseOperation") -> "OrOperation":
        return OrOperation(value=self, other_value=other)

    @abstractmethod
    def __call__(self, obj: Any) -> bool:
        pass


class AndOperation(BaseOperation):
    __slots__ = ("value", "other_value")

    def __init__(self, value: "BaseOperation", other_value: "BaseOperation") -> None:
        super().__init__(value=value)
        self.other_value = other_value

    def __call__(self, obj: Any) -> Any:
        return self.value(obj=obj) and self.other_value(obj=obj)


class OrOperation(AndOperation):
    def __call__(self, obj: Any) -> Any:
        return self.value(obj) or self.other_value(obj)


class NotOperation(BaseOperation):
    def __call__(self, obj: Any) -> bool:
        return not self.value(obj)
