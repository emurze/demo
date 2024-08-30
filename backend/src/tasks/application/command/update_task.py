from uuid import UUID

from lato import Command

from tasks.application import tasks_module
from tasks.application.exceptions import TaskNotFoundException
from tasks.domain.repositories import ITaskRepository
from tasks.domain.value_objects import TaskTitle


class UpdateTaskCommand(Command):
    id: UUID
    title: str


@tasks_module.handler(UpdateTaskCommand)
async def update_task(
    command: UpdateTaskCommand,
    repository: ITaskRepository,
) -> None:
    task = await repository.get_by_id(command.id, for_update=True)

    if task is None:
        raise TaskNotFoundException(task_id=str(command.id))

    task.update(title=TaskTitle(command.title))
