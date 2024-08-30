import abc
from typing import NoReturn


class ValueObject(abc.ABC):
    @abc.abstractmethod
    def validate(self) -> NoReturn | None: ...

    @abc.abstractmethod
    def as_generic_type(self) -> str: ...

    def __post_init__(self) -> None:
        self.validate()
