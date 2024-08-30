from fastapi import FastAPI

from config import AppConfig
from containers import create_container
from tasks.presentation.api import router as tasks_router


def create_app(config: AppConfig = AppConfig()) -> FastAPI:
    container = create_container(config)
    app = FastAPI(
        title=config.app_title,
        container=container,
    )
    app.include_router(tasks_router)
    return app
