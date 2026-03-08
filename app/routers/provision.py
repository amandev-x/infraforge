from fastapi import APIRouter, Depends
from datetime import datetime

from app.schemas.provision import ProvisionRequest, JobResponse

router = APIRouter(
    prefix="/provision",
    tags=["Provisioning"]
)

@router.post("/", response_model=JobResponse, status_code=201)
async def provision(request: ProvisionRequest):
    # For now we will be returning a dummy job response.
    return {
        "job_id": "dummy-123",
        "status": "pending",
        "module": request.module,
        "env": request.env,
        "created_at": datetime.now(),
        "logs": None
    }