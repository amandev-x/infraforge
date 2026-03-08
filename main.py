from fastapi import FastAPI
from app.routers import provision, auth, jobs

app = FastAPI(
    title="InfraForge",
    description="Self-service Infrastructure Provisioning API",
    version="1.0.0"
)

# Register all routers
app.include_router(provision.router)
app.include_router(auth.router)
app.include_router(jobs.router)
@app.get("/health")
async def health():
    return {"status": "ok", "service": "infraforge"}