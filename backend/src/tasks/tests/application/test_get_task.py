import pytest
from faker import Faker
from lato import Application

from tasks.application.command import CreateTaskCommand
from tasks.application.exceptions import TaskNotFoundException
from tasks.application.query import GetTaskQuery


@pytest.mark.integration
async def test_get_task(app: Application, faker: Faker) -> None:
    # arrange
    command = CreateTaskCommand(id=faker.uuid4(), title=faker.word())
    await app.execute_async(command)

    # act
    task_dict = await app.execute_async(GetTaskQuery(id=command.id))

    # assert
    assert task_dict == {
        "id": command.id,
        "title": command.title,
    }


@pytest.mark.integration
async def test_get_task_returns_none(app: Application, faker: Faker) -> None:
    task_id = faker.uuid4()
    with pytest.raises(TaskNotFoundException, match=task_id):
        await app.execute_async(GetTaskQuery(id=task_id))
