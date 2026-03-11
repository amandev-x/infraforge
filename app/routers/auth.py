from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse

from app.auth.jwt import create_hash_password, verify_password, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# Temporary in memory database
fake_users_db = {}

@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(request: RegisterRequest):
    # Check if user's email already exists. Will later use real DB
    if request.email in fake_users_db.values():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User with email {request.email} already exists."
        )
    
    # Generate password hash
    fake_users_db[request.email] = {
        "email": request.email,
        "hashed_password": create_hash_password(request.password)
    }

    return {"message": f"User {request.email} registered successfully!"}

@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Check if user exists 
    user = fake_users_db.get(form_data.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Verify password
    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Create and return JWT Token
    token = create_access_token({"sub": form_data.username})
    return {
        "access_token": token,
        "token_type": "bearer"
    }
