from dataclasses import dataclass
from typing import NoReturn, NewType, ClassVar
from uuid import UUID

from seedwork.domain.value_objects import ValueObject
from tasks.domain.exceptions import TitleMoreThanLimitValidationException

TaskId = NewType("TaskId", UUID)


@dataclass(frozen=True)
class TaskTitle(ValueObject):
    title: str
    MAX_LENGTH: ClassVar[int] = 256

    def as_generic_type(self) -> str:
        return self.title

    def validate(self) -> NoReturn | None:
        if len(self.title) > self.MAX_LENGTH:
            raise TitleMoreThanLimitValidationException(
                self.MAX_LENGTH,
                self.title,
            )
