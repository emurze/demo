import uuid

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Dependency, Singleton
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
    AsyncSession,
)
from lato import TransactionContext, Application

from config import AppConfig
from seedwork.infra.container.provider import ContainerProvider
from tasks.application import tasks_module
from tasks.infra.repositories import SqlAlchemyTaskRepository


def create_db_engine(config: AppConfig) -> AsyncEngine:
    from seedwork.infra.db.base import Base

    engine = create_async_engine(config.db_dsn, echo=config.db_echo)
    Base.metadata.bind = engine
    return engine


def create_application(config, db_engine) -> Application:
    application = Application(
        config.app_title,
        app_version=0.1,
        db_engine=db_engine,
    )
    application.include_submodule(tasks_module)

    @application.on_create_transaction_context
    def on_create_transaction_context(**_) -> TransactionContext:
        """Context factory"""
        engine = application.get_dependency("db_engine")
        session = AsyncSession(engine)
        correlation_id = uuid.uuid4()

        # Create IoC container for the transaction
        dependency_provider = ContainerProvider(
            TransactionContainer(
                db_session=session,
                correlation_id=correlation_id,
            )
        )
        return TransactionContext(dependency_provider)

    @application.on_exit_transaction_context
    async def on_exit_transaction_context(
        ctx: TransactionContext,
        exception: Exception | None = None,
    ) -> None:
        """Context __exit__"""
        session = ctx["db_session"]
        if exception:
            await session.rollback()
        else:
            await ctx[SqlAlchemyTaskRepository].persist_all()
            await session.commit()
        await session.close()

    return application


class ApplicationContainer(DeclarativeContainer):
    config = Dependency(instance_of=AppConfig)
    db_engine = Singleton(create_db_engine, config)
    application = Singleton(create_application, config, db_engine)


class TransactionContainer(DeclarativeContainer):
    correlation_id = Dependency(instance_of=uuid.UUID)
    db_session = Dependency(instance_of=AsyncSession)
    task_repository = Singleton(SqlAlchemyTaskRepository, db_session)


def create_container(config: AppConfig) -> ApplicationContainer:
    return ApplicationContainer(config=config)
