from fastapi import Request
from fastapi.responses import JSONResponse
from services.auth_service import AuthService

async def add_feature(request: Request, call_next):
    auth_service = AuthService()
    if not auth_service.is_authorized(request):
        return JSONResponse(content={"error": "Unauthorized"}, status_code=401)
    response = await call_next(request)
    return response