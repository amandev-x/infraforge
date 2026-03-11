from fastapi import APIRouter, Depends, status
from datetime import datetime

from app.schemas.provision import ProvisionRequest, JobResponse
from app.auth.jwt import get_current_user

router = APIRouter(
    prefix="/provision",
    tags=["Provisioning"]
)

@router.post("/", response_model=JobResponse, status_code=status.HTTP_202_ACCEPTED)
async def provision(request: ProvisionRequest, current_user: str = Depends(get_current_user)):
    # For now we will be returning a dummy job response.
    return {
        "job_id": "dummy-123",
        "status": "pending",
        "module": request.module,
        "env": request.env,
        "created_at": datetime.now(),
        "logs": None
    }