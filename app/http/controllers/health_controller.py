from fastapi import APIRouter, HTTPException, Request

from ...services.admin_user_service import AdminUserService
from ..responses.status import Status

router = APIRouter(
    tags=["health"],
    responses={
        404: Status(success=False, message="Not found").model_dump(),
    },
)


@router.get("/")
async def index() -> Status:
    return Status(success=True, message="ok")


@router.get("/healthz")
async def healthz(request: Request) -> Status:
    admin_user_service = request.app.state.injector.get(AdminUserService)

    return Status(success=True, message="ok")
