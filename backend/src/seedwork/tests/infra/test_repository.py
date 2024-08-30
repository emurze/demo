import uuid
from dataclasses import dataclass
from typing import NewType
from uuid import UUID

import pytest
from faker import Faker

from seedwork.domain.entities import Entity
from seedwork.infra.memory.repositories import InMemoryRepository

CarId = NewType("CarId", UUID)


@dataclass
class Car(Entity):
    id: CarId
    title: str


def make_car_and_repository(faker: Faker) -> tuple[Car, InMemoryRepository]:
    return (
        Car(id=CarId(uuid.uuid4()), title=faker.word()),
        InMemoryRepository(),
    )


@pytest.mark.unit
async def test_add(faker: Faker) -> None:
    # arrange
    car, repository = make_car_and_repository(faker)

    # act
    repository.add(car)

    # assert
    assert await repository.get_by_id(car.id) == car


@pytest.mark.unit
async def test_get_by_id_returns_none(faker: Faker) -> None:
    # arrange
    car, repository = make_car_and_repository(faker)

    # act
    result = await repository.get_by_id(car.id)

    # assert
    assert result is None


@pytest.mark.unit
async def test_get_by_id(faker: Faker) -> None:
    await test_add(faker)


@pytest.mark.unit
async def test_delete(faker: Faker) -> None:
    # arrange
    car, repository = make_car_and_repository(faker)

    # act
    await repository.delete(car)

    # arrange
    assert await repository.count() == 0


@pytest.mark.unit
async def test_delete_by_id(faker: Faker) -> None:
    # arrange
    car, repository = make_car_and_repository(faker)

    # act
    await repository.delete_by_id(car.id)

    # arrange
    assert await repository.count() == 0


@pytest.mark.unit
async def test_count(faker: Faker) -> None:
    await test_delete_by_id(faker)


@pytest.mark.unit
async def test_persist_two_entities(faker: Faker) -> None:
    # arrange
    car, repository = make_car_and_repository(faker)
    car2 = Car(id=CarId(uuid.uuid4()), title=faker.word())

    # act
    repository.add(car)
    repository.add(car2)

    # assert
    assert await repository.count() == 2
    assert await repository.get_by_id(car.id) == car
    assert await repository.get_by_id(car2.id) == car2
