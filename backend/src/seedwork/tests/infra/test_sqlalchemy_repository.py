import uuid
from dataclasses import dataclass
from typing import NewType

import pytest
from faker import Faker
from sqlalchemy import Column, String
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession

from conftest import db_session
from seedwork.domain.entities import Entity
from seedwork.infra.db.base import Base
from seedwork.infra.db.mapper import IDataMapper
from seedwork.infra.db.repositories import SqlAlchemyRepository
from seedwork.infra.db.utils import to_uuid

CarId = NewType("CarId", uuid.UUID)


@dataclass
class Car(Entity):
    id: CarId
    title: str


class CarModel(Base):
    __tablename__ = "cars"
    id = Column(sa.UUID, primary_key=True)
    title = Column(String(255), nullable=False)


class CarMapper(IDataMapper):
    def entity_to_model(self, entity: Car) -> CarModel:
        return CarModel(id=entity.id, title=entity.title)

    def model_to_entity(self, model: CarModel) -> Car:
        return Car(id=CarId(to_uuid(model.id)), title=model.title)


class CarSqlAlchemyRepository(SqlAlchemyRepository):
    model_class = CarModel
    mapper_class = CarMapper


def make_car_and_repository(
    db_session: AsyncSession,
) -> tuple[Car, CarSqlAlchemyRepository]:
    faker = Faker()
    return (
        Car(id=CarId(uuid.uuid4()), title=faker.name()),
        CarSqlAlchemyRepository(db_session),
    )


@pytest.mark.integration
async def test_add(db_session: AsyncSession) -> None:
    # arrange
    car, repository = make_car_and_repository(db_session)

    # act
    repository.add(car)

    # assert
    assert await repository.get_by_id(car.id) == car


@pytest.mark.integration
async def test_get_by_id(db_session: AsyncSession) -> None:
    await test_add(db_session)


@pytest.mark.integration
async def test_get_by_id_returns_none(db_session: AsyncSession) -> None:
    # arrange
    car, repository = make_car_and_repository(db_session)

    # act
    result = await repository.get_by_id(car.id)

    # assert
    assert result is None


@pytest.mark.integration
async def test_delete_by_id(db_session: AsyncSession) -> None:
    # arrange
    car, repository = make_car_and_repository(db_session)

    # act
    await repository.delete_by_id(car.id)

    # arrange
    assert await repository.count() == 0


@pytest.mark.integration
async def test_delete(db_session: AsyncSession) -> None:
    # arrange
    car, repository = make_car_and_repository(db_session)

    # act
    await repository.delete(car)

    # arrange
    assert await repository.count() == 0


@pytest.mark.integration
async def test_count(db_session: AsyncSession) -> None:
    await test_delete_by_id(db_session)


@pytest.mark.integration
async def test_persist_two_entities(
    faker: Faker,
    db_session: AsyncSession,
) -> None:
    # arrange
    car1 = Car(id=CarId(uuid.uuid4()), title=faker.word())
    car2 = Car(id=CarId(uuid.uuid4()), title=faker.word())
    repository = CarSqlAlchemyRepository(db_session)

    # act
    repository.add(car1)
    repository.add(car2)

    # assert
    assert await repository.count() == 2
    assert await repository.get_by_id(car1.id) == car1
    assert await repository.get_by_id(car2.id) == car2


@pytest.mark.integration
async def test_persistence(faker: Faker, db_session: AsyncSession) -> None:
    # arrange
    original = Car(id=CarId(uuid.uuid4()), title=faker.word())
    repository = CarSqlAlchemyRepository(db_session)

    # act
    repository.add(original)
    await repository.persist_all()

    # assert
    repository2 = CarSqlAlchemyRepository(db_session)
    persisted = await repository2.get_by_id(original.id)
    assert persisted == original
