import pytest

from tasks.domain.exceptions import (
    TitleMoreThanLimitValidationException,
    TextMoreThanLimitValidationException,
)
from teachers.domain.value_objects import (
    TeacherTitle,
    TeacherDescription,
)


@pytest.mark.unit
def test_teacher_title() -> None:
    _ = TeacherTitle("letter")


@pytest.mark.unit
def test_teacher_title_more_than_limit_error() -> None:
    with pytest.raises(TitleMoreThanLimitValidationException):
        _ = TeacherTitle("letter" * 1000)


@pytest.mark.unit
def test_teacher_description() -> None:
    _ = TeacherDescription("letter")


@pytest.mark.unit
def test_teacher_description_more_than_limit_error() -> None:
    with pytest.raises(TextMoreThanLimitValidationException):
        _ = TeacherDescription("letter" * 1000)
