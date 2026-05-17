from fastapi import Request, Response
from fastapi.responses import JSONResponse
from services.user_service import UserService

MAX_REQUESTS_PER_HOUR = 100

def check_request_limit(request: Request):
    """
    Check if the user has exceeded their request limit.

    Args:
    request (Request): The incoming request object.

    Returns:
    JSONResponse: An error response if the request limit is exceeded, otherwise None.
    """
    user_id = request.headers.get("X-User-ID")
    if not user_id:
        return JSONResponse(content={"error": "Missing X-User-ID header"}, status_code=401)

    user_service = UserService()
    user = user_service.get_user(int(user_id))
    if not user:
        return JSONResponse(content={"error": "User not found"}, status_code=404)

    # Get the current hour and the number of requests made by the user in the last hour
    current_hour = int(request.state.datetime.utcnow().timestamp() // 3600)
    requests_made = user_service.get_requests_made(user.id, current_hour)

    # Check if the user has exceeded their request limit
    if requests_made >= MAX_REQUESTS_PER_HOUR:
        return JSONResponse(content={"error": "Request limit exceeded"}, status_code=429)

    # If the user has not exceeded their request limit, increment the number of requests made
    user_service.increment_requests_made(user.id, current_hour)

    return None