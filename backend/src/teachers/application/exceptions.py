from dataclasses import dataclass

from seedwork.application.exceptions import ApplicationException


@dataclass(eq=False)
class TeacherNotFoundException(ApplicationException):
    teacher_id: str

    @property
    def message(self) -> str:
        return f"Teacher {self.teacher_id} not found"
