from fastapi import FastAPI
from routes import payment_routes, user_routes

app = FastAPI(title="Demo Payment Service")

# Include routers
app.include_router(payment_routes.router, prefix="/api/payments")
app.include_router(user_routes.router, prefix="/api/users")

@app.get("/")
def root():
    return {"message": "Demo Payment Service API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}