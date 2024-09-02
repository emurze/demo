import abc
from uuid import UUID

from seedwork.infra.db.repositories import IGenericRepository
from teachers.domain.entities import Teacher


class ITeacherRepository(abc.ABC, IGenericRepository[Teacher, UUID]):
    pass
