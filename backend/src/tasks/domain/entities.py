from dataclasses import dataclass

from seedwork.domain.entities import Entity
from tasks.domain.value_objects import TaskTitle, TaskId


@dataclass
class Task(Entity):
    id: TaskId
    title: TaskTitle

    def update(self, title: TaskTitle) -> None:
        self.title = title
