if __name__ == "__main__":
    
    import uvicorn
    from database.postgresql.base import Base
    from database.postgresql.connection import engine
    from registration.models import Users


    uvicorn.run("asgi:app", log_level="info", reload=True)