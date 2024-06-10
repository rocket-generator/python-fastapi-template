from injector import Binder, Injector, InstanceProvider, singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from ..config import Config, config
from ..libraries import Hash, JWT
from ..repositories.admin_user_repository import AdminUserRepository
from ..services.admin_user_service import AdminUserService
from ..http.middlewares.auth.admin_authentication_backend import AdminAuthenticationBackend


def build_container() -> Injector:
    return Injector(modules=[configure])


def configure(binder: Binder):
    binder.bind(Config, to=config, scope=singleton)

    engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
    session_factory = sessionmaker(autocommit=False,
                                   autoflush=False,
                                   bind=engine)
    db = scoped_session(session_factory)
    binder.bind(scoped_session, to=db)

    # Libraries
    _hash = Hash()
    binder.bind(Hash, to=_hash)

    _jwt = JWT()
    binder.bind(JWT, to=_jwt)

    # Repositories
    admin_user_repository = AdminUserRepository(db)
    binder.bind(AdminUserRepository, to=admin_user_repository)

    # Services
    admin_user_service = AdminUserService(admin_user_repository,
                                          _hash=_hash,
                                          _jwt=_jwt,
                                          _config=config)
    binder.bind(AdminUserService, to=admin_user_service)

    # Middlewares
    admin_authentication_backend = AdminAuthenticationBackend(
        _admin_user_service=admin_user_service, _jwt=_jwt, _config=config)
