from fastapi import FastAPI

from app.domain.container import Container
from app.presentation.endpoint import router


def create_app() -> FastAPI:
    container = Container()
    container.wire(packages=["app.presentation.endpoint"])

    db = container.db()
    db.create_database()

    app = FastAPI()
    app.container = container  # type: ignore[attr-defined]
    app.include_router(router)

    return app


app = create_app()
