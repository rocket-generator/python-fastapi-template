from fastapi import APIRouter, HTTPException, Request
from injector import Binder, Injector, InstanceProvider, singleton
from starlette.authentication import requires

from app.services.admin_user_service import AdminUserService
from app.http.requests.admin_sign_in import AdminSignIn
from app.http.responses.access_token import AccessToken
from app.http.responses.status import Status

router = APIRouter(
    prefix="/admin/auth",
    tags=["auth"],
    responses={
        401: Status(success=False, message="Unauthorized").dict(),
        402: Status(success=False, message="Forbidden").dict(),
        404: Status(success=False, message="Not found").dict(),
    },
)


@router.post("/signin")
async def signin(request: Request, credential: AdminSignIn) -> AccessToken:
    admin_user_service = request.app.state.injector.get(AdminUserService)

    user, token = admin_user_service.sign_in(credential.email,
                                             credential.password)

    return AccessToken(access_token=token)
