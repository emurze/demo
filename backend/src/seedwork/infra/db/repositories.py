import abc
from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from seedwork.infra.db.base import Base
from seedwork.infra.db.mapper import IDataMapper


class IGenericRepository[Entity, EntityId](metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def add(self, entity: Entity) -> EntityId: ...

    @abc.abstractmethod
    async def delete(self, entity: Entity) -> None: ...

    @abc.abstractmethod
    async def delete_by_id(self, entity_id: EntityId) -> None: ...

    @abc.abstractmethod
    async def get_by_id(
        self,
        entity_id: EntityId,
        for_update: bool = False,
    ) -> Entity | None: ...

    @abc.abstractmethod
    async def count(self) -> int: ...

    @abc.abstractmethod
    async def persist(self, entity: Entity): ...

    @abc.abstractmethod
    async def persist_all(self): ...


class Deleted:
    def __repr__(self):
        return "<Deleted entity>"

    def __str__(self):
        return "<Deleted entity>"


DELETED = Deleted()


class SqlAlchemyRepository[Entity, EntityId](IGenericRepository):
    model_class: type[Base]
    mapper_class: type[IDataMapper]

    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.identity_map: dict[UUID, Entity] = {}
        self.mapper = self.mapper_class()

    def add(self, entity: Entity) -> EntityId:
        self.identity_map[entity.id] = entity
        model = self.mapper.entity_to_model(entity)
        self.session.add(model)
        return entity.id

    async def delete(self, entity: Entity) -> None:
        await self.delete_by_id(entity.id)

    async def delete_by_id(self, entity_id: EntityId) -> None:
        self._check_not_deleted(entity_id)
        self.identity_map[entity_id] = DELETED
        if model := await self.session.get(self.model_class, entity_id):
            await self.session.delete(model)

    async def get_by_id(
        self,
        entity_id: EntityId,
        for_update: bool = False,
    ) -> Entity | None:
        model = await self.session.get(
            self.model_class,
            entity_id,
            with_for_update=for_update,
        )

        if model is None:
            return None

        entity = self.mapper.model_to_entity(model)
        self._check_not_deleted(entity_id)

        if map_entity := self.identity_map.get(entity.id):
            return map_entity

        self.identity_map[entity.id] = entity
        return entity

    async def count(self) -> int:
        query = select(func.count()).select_from(self.model_class)
        return (await self.session.execute(query)).scalar_one()

    async def persist(self, entity: Entity) -> None:
        self._check_not_deleted(entity.id)
        assert entity.id in self.identity_map, (
            "Cannon persist entity which is unknown to the repo. "
            "Did you forget to call repo.add() for this entity?"
        )
        instance = self.mapper.entity_to_model(entity)
        merged = await self.session.merge(instance)
        self.session.add(merged)

    async def persist_all(self) -> None:
        for entity in self.identity_map.values():
            if entity is not DELETED:
                await self.persist(entity)

    def _check_not_deleted(self, entity_id):
        assert (
            self.identity_map.get(entity_id) is not DELETED
        ), f"Entity {entity_id} already removed"
