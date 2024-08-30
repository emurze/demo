from lato import Application
from starlette.requests import Request

from config import AppConfig


async def get_application(request: Request) -> Application:
    return request.app.extra["container"].application()


async def get_config(request: Request) -> AppConfig:
    return request.app.extra["container"].config()
