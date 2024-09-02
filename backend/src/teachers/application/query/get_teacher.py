from typing import NoReturn
from uuid import UUID

from lato import Query
from sqlalchemy.ext.asyncio import AsyncSession

from teachers.application import teachers_module
from teachers.application.exceptions import TeacherNotFoundException
from teachers.application.query.map_teacher_to_dao import (
    map_teacher_model_to_dao,
)
from teachers.infra.repositories import TeacherModel


class GetTeacherQuery(Query):
    id: UUID


@teachers_module.handler(GetTeacherQuery)
async def get_teacher(
    query: GetTeacherQuery,
    db_session: AsyncSession,
) -> dict | NoReturn:
    teacher_model: TeacherModel | None = await db_session.get(
        TeacherModel,
        query.id,
    )

    if teacher_model is None:
        raise TeacherNotFoundException(str(query.id))

    return map_teacher_model_to_dao(teacher_model)
