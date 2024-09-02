from uuid import UUID

from fastapi import APIRouter

router = APIRouter()


@router.get("/{teacher_id}")
async def get_teacher(teacher_id: UUID):
    pass


@router.get("/")
async def get_teachers():
    pass


@router.get("/")
async def create_teacher():
    pass
