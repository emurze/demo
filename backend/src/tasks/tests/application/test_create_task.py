import pytest
from faker import Faker

from tasks.application.command import CreateTaskCommand
from tasks.application.command.create_task import create_task
from tasks.tests.application.conftest import MemoryTaskRepository


@pytest.mark.unit
async def test_create_task(faker: Faker) -> None:
    # arrange
    command = CreateTaskCommand(title=faker.word())
    repository = MemoryTaskRepository()

    # act
    await create_task(command, repository)

    # assert
    assert await repository.count() == 1
