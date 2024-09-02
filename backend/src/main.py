from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config import AppConfig
from containers import create_container
from tasks.presentation.api import router as tasks_router
from teachers.presentation.api import router as teachers_router


def create_app(config: AppConfig = AppConfig()) -> FastAPI:
    container = create_container(config)
    app = FastAPI(
        title=config.app_title,
        container=container,
    )
    app.include_router(tasks_router)
    app.include_router(teachers_router)
    app.add_middleware(
        CORSMiddleware,  # noqa
        allow_origins=config.allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
