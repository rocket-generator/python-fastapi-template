from logging import getLogger

from injector import Binder, Injector, InstanceProvider, singleton
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from ..config import Config, config
from ..http.middlewares.auth.admin_authentication_backend import \
    AdminAuthenticationBackend
from ..interfaces.libraries.access_token_interface import AccessTokenInterface
from ..interfaces.libraries.hash_interface import HashInterface
from ..interfaces.repositories.admin_user_repository_interface import \
    AdminUserRepositoryInterface
from ..interfaces.services.admin_user_service_interface import \
    AdminUserServiceInterface
from ..interfaces.usecases.get_admin_me_usecase_interface import \
    GetAdminMeUsecaseInterface
from ..interfaces.usecases.put_admin_me_usecase_interface import \
    PutAdminMeUsecaseInterface
from ..libraries import AccessToken, Hash
from ..repositories.admin_user_repository import AdminUserRepository
from ..services.admin_user_service import AdminUserService
from ..usecases.get_admin_me_usecase import GetAdminMeUsecase
from ..usecases.put_admin_me_usecase import PutAdminMeUsecase

# /* [IMPORT_REPOSITORY_INTERFACES] */

# /* [IMPORT_SERVER_INTERFACES] */

# /* [IMPORT_USECASE_INTERFACES] */

# /* [IMPORT_REPOSITORIES] */

# /* [IMPORT_SERVERS] */

# /* [IMPORT_USECASES] */



def build_container() -> Injector:
    return Injector(modules=[configure])


def configure(binder: Binder):
    binder.bind(Config, to=config, scope=singleton)

    logger = getLogger(__name__)

    engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
    engine = engine.execution_options(isolation_level="AUTOCOMMIT")
    session_factory = sessionmaker(autoflush=True, bind=engine)
    db = scoped_session(session_factory)
    binder.bind(scoped_session, to=db, scope=singleton)

    # Libraries
    _hash = Hash(logger=logger)
    binder.bind(HashInterface, to=_hash)

    _access_token = AccessToken(logger=logger)
    binder.bind(AccessTokenInterface, to=_access_token)

    # Repositories
    admin_user_repository = AdminUserRepository(db)
    binder.bind(AdminUserRepositoryInterface, to=admin_user_repository)

    # /* [REGISTER_REPOSITORIES] */

    # Services
    admin_user_service = AdminUserService(admin_user_repository,
                                          _hash=_hash,
                                          _access_token=_access_token,
                                          _config=config)
    binder.bind(AdminUserServiceInterface, to=admin_user_service)

    # /* [REGISTER_SERVICES] */

    # UseCases
    put_admin_user_use_case = PutAdminMeUsecase(
        admin_user_service=admin_user_service)
    binder.bind(PutAdminMeUsecaseInterface, to=put_admin_user_use_case)

    get_admin_user_use_case = GetAdminMeUsecase(
        admin_user_service=admin_user_service)
    binder.bind(GetAdminMeUsecaseInterface, to=get_admin_user_use_case)

    # /* [REGISTER_USECASES] */

    # Middlewares
    admin_authentication_backend = AdminAuthenticationBackend(
        _admin_user_service=admin_user_service, _config=config)
    binder.bind(AdminAuthenticationBackend, to=admin_authentication_backend)
