from contextlib import suppress
from typing import Any

from seedwork.infra.db.repositories import IGenericRepository
from seedwork.domain.entities import Entity as BaseEntity


class InMemoryRepository[Entity, EntityId](IGenericRepository):
    def __init__(self) -> None:
        self.objects: dict[Any, Any] = {}

    def add(self, entity: Entity) -> None:
        assert issubclass(entity.__class__, BaseEntity)
        self.objects[entity.id] = entity

    async def get_by_id(
        self,
        entity_id: EntityId,
        for_update: bool = False,
    ) -> Entity | None:
        try:
            return self.objects[entity_id]
        except KeyError:
            return None

    async def delete_by_id(self, entity_id: EntityId) -> None:
        with suppress(KeyError):
            del self.objects[entity_id]

    async def delete(self, entity: Entity):
        with suppress(KeyError):
            del self.objects[entity.id]

    async def count(self):
        return len(self.objects)

    async def persist(self, entity: Entity) -> None: ...

    async def persist_all(self) -> None: ...
