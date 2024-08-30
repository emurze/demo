from typing import NoReturn

from lato import Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from tasks.application import tasks_module
from tasks.application.query.model_mappers import map_task_model_to_dao
from tasks.infra.repositories import TaskModel


class GetTasksQuery(Query):
    pass


@tasks_module.handler(GetTasksQuery)
async def get_tasks(
    _: GetTasksQuery,
    db_session: AsyncSession,
) -> dict | NoReturn:
    task_models = await db_session.execute(select(TaskModel))
    return [map_task_model_to_dao(model) for model in task_models.scalars()]
