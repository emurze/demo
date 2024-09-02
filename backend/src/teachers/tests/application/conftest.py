from seedwork.infra.memory.repositories import InMemoryRepository
from teachers.domain.repositories import ITeacherRepository


class MemoryTeacherRepository(InMemoryRepository, ITeacherRepository):
    pass
