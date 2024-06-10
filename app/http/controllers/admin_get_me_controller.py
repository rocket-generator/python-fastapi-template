from fastapi import APIRouter, HTTPException, Request
from injector import Binder, Injector, InstanceProvider, singleton
from starlette.authentication import requires

from app.http.responses.admin_me import AdminMe
from app.services.admin_user_service import AdminUserService
from app.http.requests.admin_sign_in import AdminSignIn
from app.http.responses.access_token import AccessToken
from app.http.responses.status import Status

router = APIRouter(
    prefix="/admin",
    tags=["me"],
    responses={
        401: Status(success=False, message="Unauthorized").dict(),
        402: Status(success=False, message="Forbidden").dict(),
        404: Status(success=False, message="Not found").dict(),
    },
)


@router.get("/me")
@requires(["admin_authenticated"])
async def signin(request: Request, credential: AdminSignIn) -> AdminMe:
    me = request.user
    return AdminMe.from_model(me)
