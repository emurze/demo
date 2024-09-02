import uuid
from dataclasses import field

from lato import Command

from teachers.application import teachers_module
from teachers.domain.entities import Teacher
from teachers.domain.repositories import ITeacherRepository
from teachers.domain.value_objects import (
    TeacherId,
    TeacherTitle,
    TeacherDescription,
    TeacherDifficulty,
)


class CreateTeacherCommand(Command):
    title: str
    description: str
    difficulty: str


@teachers_module.handler(CreateTeacherCommand)
async def create_teacher(
    command: CreateTeacherCommand,
    teachers_repository: ITeacherRepository,
) -> uuid.UUID:
    teacher_id = TeacherId(command.id)
    title = TeacherTitle(command.title)
    description = TeacherDescription(command.description)
    difficulty = TeacherDifficulty(command.difficulty)
    teacher = Teacher(
        id=teacher_id,
        title=title,
        description=description,
        difficulty=difficulty,
    )
    teachers_repository.add(teacher)
    return teacher_id
