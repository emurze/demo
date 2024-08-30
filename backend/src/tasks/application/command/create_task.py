import uuid

from lato import Command

from tasks.application import tasks_module
from tasks.domain.entities import Task
from tasks.domain.repositories import ITaskRepository
from tasks.domain.value_objects import TaskId, TaskTitle


class CreateTaskCommand(Command):
    title: str


@tasks_module.handler(CreateTaskCommand)
async def create_task(
    command: CreateTaskCommand,
    task_repository: ITaskRepository,
) -> uuid.UUID:
    task_id = TaskId(command.id)
    title = TaskTitle(command.title)
    task = Task(id=task_id, title=title)
    task_repository.add(task)
    return task.id
