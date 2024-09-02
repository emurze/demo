import reprlib
from dataclasses import dataclass

from seedwork.domain.exceptions import DomainException


@dataclass(eq=False)
class TitleMoreThanLimitValidationException(DomainException):
    limit: int
    title: str

    @property
    def message(self) -> str:
        return (
            f"Title <{reprlib.repr(self.title)}> is more "
            f"than {self.limit} characters"
        )


@dataclass(eq=False)
class TextMoreThanLimitValidationException(DomainException):
    limit: int
    text: str

    @property
    def message(self) -> str:
        return (
            f"Text <{reprlib.repr(self.text)}> is more "
            f"than {self.limit} characters"
        )
