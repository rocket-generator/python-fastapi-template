from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware

from app.http.controllers.admin_auth_controller import router as admin_auth_controller
from app.http.controllers.health_controller import router as health_controller
from app.http.controllers.admin_get_me_controller import router as admin_get_me_controller

from app.http.middlewares.auth.admin_authentication_backend import AdminAuthenticationBackend
from .container import build_container
from injector import Injector


def create_app():
    injector = build_container()
    app = FastAPI(title="Fast API Template", )
    app.state.injector = injector
    app = _setup_middleware(app, injector)
    app = _setup_router(app, injector)

    return app


def _setup_middleware(app: FastAPI, injector: Injector) -> FastAPI:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_middleware(GZipMiddleware, minimum_size=1000)

    authentication_backend = injector.get(AdminAuthenticationBackend)
    app.add_middleware(AuthenticationMiddleware,
                       backend=authentication_backend)

    return app


def _setup_router(app: FastAPI, injector: Injector) -> FastAPI:
    app.include_router(health_controller)
    app.include_router(admin_auth_controller)
    app.include_router(admin_get_me_controller)
    return app
