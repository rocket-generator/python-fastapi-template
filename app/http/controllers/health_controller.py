from fastapi import APIRouter, HTTPException, Request
from injector import Binder, Injector, InstanceProvider, singleton
from ..responses.status import Status
from ...services.admin_user_service import AdminUserService

router = APIRouter(
    tags=["health"],
    responses={404: {
        "description": "Not found"
    }},
)


@router.get("/")
async def signin() -> Status:
    return Status(success=True, message="ok")


@router.get("/healthz")
async def healthz(request: Request) -> Status:
    admin_user_service = request.app.state.injector.get(AdminUserService)

    return Status(success=True, message="ok")
