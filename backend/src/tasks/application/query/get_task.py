from typing import NoReturn
from uuid import UUID

from lato import Query
from sqlalchemy.ext.asyncio import AsyncSession

from tasks.application import tasks_module
from tasks.application.exceptions import TaskNotFoundException
from tasks.application.query.model_mappers import map_task_model_to_dao
from tasks.infra.repositories import TaskModel


class GetTaskQuery(Query):
    id: UUID


@tasks_module.handler(GetTaskQuery)
async def get_task(
    query: GetTaskQuery,
    db_session: AsyncSession,
) -> dict | NoReturn:
    task_model: TaskModel | None = await db_session.get(TaskModel, query.id)

    if task_model is None:
        raise TaskNotFoundException(str(query.id))

    return map_task_model_to_dao(task_model)
