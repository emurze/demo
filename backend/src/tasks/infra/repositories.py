from sqlalchemy import Column, UUID, String

from seedwork.infra.db.base import Base
from seedwork.infra.db.mapper import IDataMapper
from seedwork.infra.db.repositories import SqlAlchemyRepository
from tasks.domain.entities import Task
from tasks.domain.repositories import ITaskRepository
from tasks.domain.value_objects import TaskTitle, TaskId


class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(UUID, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255))


class TaskMapper(IDataMapper):
    def entity_to_model(self, entity: Task) -> TaskModel:
        return TaskModel(id=entity.id, title=entity.title.as_generic_type())

    def model_to_entity(self, model: TaskModel) -> Task:
        return Task(id=TaskId(model.id), title=TaskTitle(model.title))


class SqlAlchemyTaskRepository(ITaskRepository, SqlAlchemyRepository):
    model_class = TaskModel
    mapper_class = TaskMapper
