from faker.utils.text import slugify
from sqlalchemy import Column, UUID, String

from seedwork.infra.db.base import Base
from seedwork.infra.db.mapper import IDataMapper
from seedwork.infra.db.repositories import SqlAlchemyRepository
from teachers.domain.entities import Teacher
from teachers.domain.repositories import ITeacherRepository
from teachers.domain.value_objects import (
    TeacherId,
    TeacherTitle,
    TeacherDescription,
    TeacherDifficulty,
)


class TeacherModel(Base):
    __tablename__ = "teachers"
    id = Column(UUID, primary_key=True)
    title = Column(String(255), nullable=False)
    slug = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    difficulty = Column(String(255), nullable=True)


class TeacherMapper(IDataMapper):
    def entity_to_model(self, entity: Teacher) -> TeacherModel:
        title = entity.title.as_generic_type()
        return TeacherModel(
            id=entity.id,
            title=title,
            slug=slugify(title),
            description=entity.description.as_generic_type(),
            difficulty=entity.difficulty.as_generic_type(),
        )

    def model_to_entity(self, model: TeacherModel) -> Teacher:
        return Teacher(
            id=TeacherId(model.id),
            title=TeacherTitle(model.title),
            description=TeacherDescription(model.description),
            difficulty=TeacherDifficulty(model.difficulty),
        )


class SqlAlchemyTaskRepository(ITeacherRepository, SqlAlchemyRepository):
    model_class = TeacherModel
    mapper_class = TeacherMapper
