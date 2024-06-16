from fastapi import APIRouter, HTTPException, Request
from injector import Binder, Injector, InstanceProvider, singleton
from starlette.authentication import requires

from app.http.requests.admin_sign_in import AdminSignIn
from app.http.responses.access_token import AccessToken
from app.http.responses.status import Status
from app.services.admin_user_service import AdminUserService

router = APIRouter(
    prefix="/admin/auth",
    tags=["auth"],
    responses={
        401: Status(success=False, message="Unauthorized").model_dump(),
        402: Status(success=False, message="Forbidden").model_dump(),
        404: Status(success=False, message="Not found").model_dump(),
    },
)


@router.post("/signin")
async def signin(request: Request, credential: AdminSignIn) -> AccessToken:
    admin_user_service = request.app.state.injector.get(AdminUserService)

    user, token = admin_user_service.sign_in(credential.email,
                                             credential.password)
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return AccessToken(access_token=token)
