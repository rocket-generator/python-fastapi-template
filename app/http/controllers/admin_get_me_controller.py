from fastapi import APIRouter, HTTPException, Query, Request
from starlette.authentication import requires

from app.http.requests.admin_sign_in import AdminSignIn
from app.http.responses.admin_me import AdminMe
from app.http.responses.status import Status

from ...interfaces.usecases.get_admin_me_usecase_interface import \
    GetAdminMeUsecaseInterface

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
async def admin_get_me(request: Request, ) -> AdminMe:
    usecase = request.app.state.injector.get(GetAdminMeUsecaseInterface)
    me = request.user
    me = usecase.handle(me.id)
    return AdminMe.from_model(me)
