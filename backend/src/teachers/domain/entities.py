from dataclasses import dataclass

from seedwork.domain.entities import Entity
from teachers.domain.value_objects import (
    TeacherId,
    TeacherTitle,
    TeacherDifficulty,
    TeacherDescription,
)


@dataclass(kw_only=True)
class Teacher(Entity):
    id: TeacherId
    title: TeacherTitle
    description: TeacherDescription | None = None
    difficulty: TeacherDifficulty  # todo: make enum in value_objects
