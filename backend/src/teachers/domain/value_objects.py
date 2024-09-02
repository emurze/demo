from dataclasses import dataclass
from typing import NewType, ClassVar, NoReturn
from uuid import UUID

from seedwork.domain.value_objects import ValueObject
from tasks.domain.exceptions import (
    TitleMoreThanLimitValidationException,
    TextMoreThanLimitValidationException,
)

TeacherId = NewType("TaskId", UUID)


@dataclass(frozen=True)
class TeacherTitle(ValueObject):
    title: str
    MAX_LENGTH: ClassVar[int] = 256

    def as_generic_type(self) -> str:
        return self.title

    def validate(self) -> NoReturn | None:
        if len(self.title) > self.MAX_LENGTH:
            raise TitleMoreThanLimitValidationException(
                self.MAX_LENGTH, self.title
            )


@dataclass(frozen=True)
class TeacherDifficulty(ValueObject):  # todo: add validation
    difficulty: str

    def as_generic_type(self) -> str:
        return self.difficulty

    def validate(self) -> NoReturn | None:
        pass


@dataclass(frozen=True)
class TeacherDescription(ValueObject):  # todo: add validation
    description: str
    MAX_LENGTH: ClassVar[int] = 256

    def as_generic_type(self) -> str:
        return self.description

    def validate(self) -> NoReturn | None:
        if len(self.description) > self.MAX_LENGTH:
            raise TextMoreThanLimitValidationException(
                self.MAX_LENGTH,
                self.description,
            )
