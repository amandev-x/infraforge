from pydantic import BaseModel, Field, field_validator  # validator is deprecated
from typing import Dict, Literal, Optional
from datetime import datetime
import uuid

# REQUEST SCHEMAS

class ProvisionRequest(BaseModel):
    module: Literal["ec2", "vpc", "s3"]
    env: Literal["dev", "staging", "prod"]
    variables: Dict[str, str] = Field(..., min_length=1)

    @field_validator("variables")
    @classmethod
    def check_no_injection(cls, v):
        dangerous = [";", "<", ">", ",", "$", "?", "|"]
        for key, val in v.items():
            if any(c in val for c in dangerous):
                raise ValueError(f"Injection detected in {key}")
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "module": "ec2",
                "env": "dev",
                "variables": {
                    "region": "us-east-1",
                    "instance_type": "t3.micro",
                }
            }
        }

class DestoryRequest(BaseModel):
    job_id: str # Destroy by referencing provision id
    env: Literal["env", "staging", "prod"]

# RESPONSE SCHEMAS

class JobResponse(BaseModel):
    job_id: str 
    status: str
    module: str 
    env: str 
    created_at: datetime
    logs: Optional[str] = None 

    class Config:
        from_attributes = True # Allows converting DB Model --> this schema directly
        


