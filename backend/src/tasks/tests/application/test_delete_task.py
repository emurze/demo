import uuid

import pytest
from faker import Faker

from tasks.application.command.delete_task import (
    delete_task,
    DeleteTaskCommand,
)
from tasks.domain.entities import Task
from tasks.domain.value_objects import TaskId, TaskTitle
from tasks.tests.application.conftest import MemoryTaskRepository


@pytest.mark.unit
async def test_delete_task(faker: Faker) -> None:
    # arrange
    task = Task(id=TaskId(uuid.uuid4()), title=TaskTitle(faker.word()))
    repository = MemoryTaskRepository()
    repository.add(task)

    # act
    command = DeleteTaskCommand(id=task.id, title=task.title)
    await delete_task(command, repository)

    # assert
    assert await repository.count() == 0
