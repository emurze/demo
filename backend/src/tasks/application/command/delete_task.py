from uuid import UUID

from lato import Command

from tasks.application import tasks_module
from tasks.domain.repositories import ITaskRepository


class DeleteTaskCommand(Command):
    id: UUID


@tasks_module.handler(DeleteTaskCommand)
async def delete_task(
    command: DeleteTaskCommand,
    repository: ITaskRepository,
) -> None:
    await repository.delete_by_id(command.id)
