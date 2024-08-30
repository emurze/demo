import abc
from uuid import UUID

from seedwork.infra.db.repositories import IGenericRepository
from tasks.domain.entities import Task


class ITaskRepository(abc.ABC, IGenericRepository[Task, UUID]):
    pass
