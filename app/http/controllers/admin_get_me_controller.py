from fastapi import APIRouter, HTTPException, Request
from starlette.authentication import requires

from app.http.requests.admin_sign_in import AdminSignIn
from app.http.responses.admin_me import AdminMe
from app.http.responses.status import Status

router = APIRouter(
    prefix="/admin",
    tags=["me"],
    responses={
        401: Status(success=False, message="Unauthorized").model_dump(),
        402: Status(success=False, message="Forbidden").model_dump(),
        404: Status(success=False, message="Not found").model_dump(),
    },
)


@router.get("/me")
@requires(["admin_authenticated"])
async def admin_get_me(request: Request, credential: AdminSignIn) -> AdminMe:
    me = request.user
    return AdminMe.from_model(me)
