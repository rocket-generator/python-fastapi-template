from fastapi import APIRouter, HTTPException, Request
from starlette.authentication import requires

from ...http.requests.update_me import UpdateMe
from ...http.responses.admin_me import AdminMe
from ...http.responses.status import Status
from ...interfaces.usecases.put_admin_me_usecase_interface import \
    PutAdminMeUsecaseInterface

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
async def admin_put_me(request: Request, data: UpdateMe) -> AdminMe:
    usecase = request.app.state.injector.get(PutAdminMeUsecaseInterface)
    me = request.user
    me = usecase.handle(me.id, data.model_dump())
    return AdminMe.from_model(me)
