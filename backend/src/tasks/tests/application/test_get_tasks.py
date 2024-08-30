from uuid import UUID

import pytest
from faker import Faker
from lato import Application, Command

from tasks.application.command import CreateTaskCommand
from tasks.application.query import GetTasksQuery


async def make_task(app: Application, task_id: UUID, title: str) -> Command:
    command = CreateTaskCommand(id=task_id, title=title)
    await app.execute_async(command)
    return command


@pytest.mark.integration
async def test_get_tasks(app: Application, faker: Faker) -> None:
    # arrange
    cmd1 = await make_task(app, task_id=faker.uuid4(), title=faker.word())
    cmd2 = await make_task(app, task_id=faker.uuid4(), title=faker.word())

    # act
    task1, task2 = await app.execute_async(GetTasksQuery())

    # assert
    assert task1 == {"id": cmd1.id, "title": cmd1.title}
    assert task2 == {"id": cmd2.id, "title": cmd2.title}
