from typing import NoReturn

from lato import Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from teachers.application import teachers_module
from teachers.application.query.map_teacher_to_dao import (
    map_teacher_model_to_dao,
)
from teachers.infra.repositories import TeacherModel


class GetTeachersQuery(Query):
    pass


@teachers_module.handler(GetTeachersQuery)
async def get_teachers(
    _: GetTeachersQuery,
    db_session: AsyncSession,
) -> dict | NoReturn:
    teacher_models = await db_session.execute(select(TeacherModel))
    return [
        map_teacher_model_to_dao(model) for model in teacher_models.scalars()
    ]
