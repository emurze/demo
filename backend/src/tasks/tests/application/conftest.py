from seedwork.infra.memory.repositories import InMemoryRepository
from tasks.domain.repositories import ITaskRepository


class MemoryTaskRepository(InMemoryRepository, ITaskRepository):
    pass
