import uuid

import pytest
from faker import Faker
from httpx import AsyncClient, Response
from starlette import status


async def get_task(api_client: AsyncClient, task_id: uuid.UUID) -> Response:
    return await api_client.get(f"/tasks/{task_id}")


async def make_task(api_client: AsyncClient, title: str) -> Response:
    return await api_client.post("/tasks/", json={"title": title})


@pytest.mark.e2e
async def test_create_task(api_client: AsyncClient, faker: Faker) -> None:
    # act
    response = await make_task(api_client, title=faker.word())

    # assert
    assert response.status_code == status.HTTP_201_CREATED
    response2 = await get_task(api_client, response.json()["id"])
    assert response2.status_code == status.HTTP_200_OK


@pytest.mark.e2e
async def test_get_task(api_client: AsyncClient, faker: Faker) -> None:
    # arrange
    task_title = faker.word()
    response = await api_client.post("/tasks/", json={"title": task_title})
    task_id = response.json()["id"]

    # act
    response = await api_client.get(f"/tasks/{task_id}")
    json_response = response.json()

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert json_response == {"id": task_id, "title": task_title}


@pytest.mark.e2e
async def test_get_task_not_found(api_client: AsyncClient) -> None:
    # act
    response = await api_client.get(f"/tasks/{uuid.uuid4()}")

    # assert
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.e2e
async def test_get_tasks(api_client: AsyncClient, faker: Faker) -> None:
    # arrange
    title1 = faker.word()
    title2 = faker.word()
    response1 = await make_task(api_client, title=title1)
    response2 = await make_task(api_client, title=title2)

    # act
    response = await api_client.get(f"/tasks/")
    json_response = response.json()

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert json_response == [
        {"id": response1.json()["id"], "title": title1},
        {"id": response2.json()["id"], "title": title2},
    ]


@pytest.mark.e2e
async def test_update_task(api_client: AsyncClient, faker: Faker) -> None:
    # arrange
    title1 = faker.word()
    response1 = await make_task(api_client, title=title1)

    # act
    title2 = faker.word()
    response = await api_client.put(
        f"/tasks/{response1.json()['id']}",
        json={"title": title2},
    )

    # assert
    assert response.status_code == status.HTTP_200_OK
    assert not response.json()

    response2 = await get_task(api_client, response1.json()["id"])
    assert response2.status_code == status.HTTP_200_OK
    assert response2.json()["title"] == title2


@pytest.mark.e2e
async def test_update_task_creates_task(
    api_client: AsyncClient,
    faker: Faker,
) -> None:
    # arrange
    task_id = uuid.uuid4()
    title = faker.word()

    # act
    response = await api_client.put(
        f"/tasks/{task_id}",
        json={"title": title},
    )

    # assert
    assert response.status_code == status.HTTP_201_CREATED
    assert not response.json()

    response2 = await get_task(api_client, task_id)
    assert response2.status_code == status.HTTP_200_OK


@pytest.mark.e2e
async def test_update_task_creates_task(
    api_client: AsyncClient,
    faker: Faker,
) -> None:
    # arrange
    title1 = faker.word()
    response1 = await make_task(api_client, title=title1)
    task_id = response1.json()["id"]

    # act
    response = await api_client.delete(f"/tasks/{task_id}")

    # assert
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not response.json()

    response2 = await get_task(api_client, task_id)
    assert response2.status_code == status.HTTP_404_NOT_FOUND
