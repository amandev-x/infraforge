from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime

from app.schemas.provision import JobResponse

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"] 
)

@router.get("/job/{job_id}", response_model=JobResponse, status_code=status.HTTP_200_OK)
async def get_job(job_id: str):
    # Dummy for Now - Will implement real DB lookup.
    if job_id != "dummy-123":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Job with ID {job_id} not found"
        )
    
    return {
        "job_id": job_id,
        "status": "running",
        "module": "ec2",
        "env": "dev",
        "created_at": datetime.now(),
        "logs": None
    }