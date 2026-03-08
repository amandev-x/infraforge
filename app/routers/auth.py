from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest):
    # Will implement real logic 
    return {"message": f"User {request.email} registered successfully!"}

@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(request: LoginRequest):
    # Will implement real logic
    return {
        "access_token": "dummy-token",
        "token_type": "bearer"
    }
