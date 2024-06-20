from fastapi import APIRouter, HTTPException, Request
from starlette.authentication import requires

from app.http.requests.update_me import UpdateMe
from app.http.responses.admin_me import AdminMe
from app.http.responses.status import Status
from app.services.admin_user_service import AdminUserService

router = APIRouter(
    prefix="/admin",
    tags=["me"],
    responses={
        401: Status(success=False, message="Unauthorized").model_dump(),
        402: Status(success=False, message="Forbidden").model_dump(),
        404: Status(success=False, message="Not found").model_dump(),
    },
)


@router.put("/me")
@requires(["admin_authenticated"])
async def admin_put_me(request: Request, credential: UpdateMe) -> AdminMe:
    admin_user_service = request.app.state.injector.get(AdminUserService)
    me = request.user
    me = admin_user_service.update_me(me, credential.model_dump())
    return AdminMe.from_model(me)
