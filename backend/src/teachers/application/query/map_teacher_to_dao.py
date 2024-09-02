from teachers.infra.repositories import TeacherModel


def map_teacher_model_to_dao(teacher_model: TeacherModel) -> dict:
    return dict(
        id=teacher_model.id,
        title=teacher_model.title,
        slug=teacher_model.slug,
        description=teacher_model.description,
        difficulty=teacher_model.difficulty,
        updated_at=teacher_model.updated_at,
        created_at=teacher_model.created_at,
    )
