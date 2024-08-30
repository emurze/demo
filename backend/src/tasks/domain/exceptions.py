import reprlib
from dataclasses import dataclass

from seedwork.domain.exceptions import DomainException


@dataclass(eq=False)
class TitleMoreThan256ValidationException(DomainException):
    title: str

    @property
    def message(self) -> str:
        return (
            f"Title <{reprlib.repr(self.title)}> is more than 256 characters"
        )
