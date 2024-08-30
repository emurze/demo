from uuid import UUID

from pydantic import BaseModel


class TaskResponseSchema(BaseModel):
    id: UUID
    title: str


class TaskRequestCreateSchema(BaseModel):
    title: str


class TaskResponseCreateSchema(BaseModel):
    id: UUID
