from tasks.infra.repositories import TaskModel


def map_task_model_to_dao(instance: TaskModel) -> dict:
    return dict(
        id=instance.id,
        title=instance.title,
    )
