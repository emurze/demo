import pytest
from faker import Faker

from teachers.application.command.create_teacher import (
    create_teacher,
    CreateTeacherCommand,
)
from teachers.tests.application.conftest import MemoryTeacherRepository


@pytest.mark.unit
async def test_create_teacher(faker: Faker) -> None:
    # arrange
    command = CreateTeacherCommand(
        title=faker.word(),
        description=faker.text(max_nb_chars=100),
        difficulty="low",
    )
    repository = MemoryTeacherRepository()

    # act
    await create_teacher(command, repository)

    # assert
    assert await repository.count() == 1
