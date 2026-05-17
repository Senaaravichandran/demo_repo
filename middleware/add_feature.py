from fastapi import Request, Response
from fastapi.responses import JSONResponse
from services.auth_service import get_user_from_token

async def add_feature_middleware(request: Request, call_next):
    token = request.headers.get("Authorization")
    if not token:
        return JSONResponse({"error": "Unauthorized"}, status_code=401)
    
    user = await get_user_from_token(token)
    if not user or not user.is_premium:
        return JSONResponse({"error": "Premium feature"}, status_code=403)
    
    response = await call_next(request)
    return response