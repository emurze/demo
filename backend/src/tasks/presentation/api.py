from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from lato import Application
from starlette import status
from starlette.responses import JSONResponse

from dependencies import get_application
from seedwork.application.exceptions import ApplicationException
from seedwork.domain.exceptions import DomainException
from seedwork.presentation.schemas import ErrorSchema
from tasks.application.command import CreateTaskCommand, UpdateTaskCommand
from tasks.application.command.delete_task import DeleteTaskCommand
from tasks.application.exceptions import TaskNotFoundException
from tasks.application.query import GetTaskQuery, GetTasksQuery
from tasks.presentation.schemas import (
    TaskResponseSchema,
    TaskResponseCreateSchema,
    TaskRequestCreateSchema,
)

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
    response_model=TaskResponseSchema,
    responses={
        status.HTTP_404_NOT_FOUND: {"model": ErrorSchema},
    },
)
async def get_task(
    task_id: UUID,
    app: Application = Depends(get_application),
):
    query = GetTaskQuery(id=task_id)

    try:
        task_dict = await app.execute_async(query)
    except TaskNotFoundException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )

    return task_dict


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[TaskResponseSchema],
)
async def get_tasks(
    app: Application = Depends(get_application),
):
    query = GetTasksQuery()
    tasks: list[dict] = await app.execute_async(query)
    return tasks


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=TaskResponseCreateSchema,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def create_task(
    schema: TaskRequestCreateSchema,
    app: Application = Depends(get_application),
):
    command = CreateTaskCommand(title=schema.title)

    try:
        task_id = await app.execute_async(command)
    except (DomainException, ApplicationException) as e:
        # TODO: add more exceptions, find specification
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": e.message},
        )

    return {"id": task_id}


@router.put(
    "/{task_id}",
    status_code=status.HTTP_200_OK,
    response_model=None,
    responses={
        status.HTTP_201_CREATED: {"model": None},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def update_task(
    task_id: UUID,
    schema: TaskRequestCreateSchema,
    app: Application = Depends(get_application),
):
    # TODO: refactor return format and status code
    command = UpdateTaskCommand(id=task_id, title=schema.title)

    try:
        await app.execute_async(command)
        return JSONResponse(content={}, status_code=status.HTTP_200_OK)

    except TaskNotFoundException:
        command2 = CreateTaskCommand(id=task_id, title=schema.title)
        await app.execute_async(command2)
        return JSONResponse(content={}, status_code=status.HTTP_201_CREATED)

    except (DomainException, ApplicationException) as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": e.message},
        )


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    responses={
        status.HTTP_400_BAD_REQUEST: {"model": ErrorSchema},
    },
)
async def delete_task(
    task_id: UUID,
    app: Application = Depends(get_application),
):
    command = DeleteTaskCommand(id=task_id)
    await app.execute_async(command)
    return JSONResponse(content={}, status_code=status.HTTP_204_NO_CONTENT)
