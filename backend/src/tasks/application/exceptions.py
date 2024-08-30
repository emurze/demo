from dataclasses import dataclass

from seedwork.application.exceptions import ApplicationException


@dataclass(eq=False)
class TaskNotFoundException(ApplicationException):
    task_id: str

    @property
    def message(self) -> str:
        return f"Task with {self.task_id} not found"
