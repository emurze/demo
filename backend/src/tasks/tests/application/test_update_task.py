import uuid

import pytest
from faker import Faker

from tasks.application.command.update_task import (
    update_task,
    UpdateTaskCommand,
)
from tasks.application.exceptions import TaskNotFoundException
from tasks.domain.entities import Task
from tasks.domain.value_objects import TaskTitle, TaskId
from tasks.tests.application.conftest import MemoryTaskRepository


@pytest.mark.unit
async def test_update_task(faker: Faker) -> None:
    # arrange
    task = Task(id=TaskId(uuid.uuid4()), title=TaskTitle(faker.word()))
    repository = MemoryTaskRepository()
    repository.add(task)

    # act
    command = UpdateTaskCommand(id=task.id, title=faker.word())
    await update_task(command, repository)
    await repository.persist_all()

    # assert
    updated_task = await repository.get_by_id(task.id)
    assert updated_task.title.as_generic_type() == command.title


@pytest.mark.unit
async def test_update_task_not_found(faker: Faker) -> None:
    # arrange
    repository = MemoryTaskRepository()

    # act & assert
    command = UpdateTaskCommand(id=uuid.uuid4(), title=faker.word())
    with pytest.raises(TaskNotFoundException):
        await update_task(command, repository)
