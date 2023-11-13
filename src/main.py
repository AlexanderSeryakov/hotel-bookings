import uvicorn
from fastapi import FastAPI

from api.booking_router import booking_router

app = FastAPI(title="Online-booking")

app.include_router(booking_router, prefix="/booking")


@app.get("/", include_in_schema=False)
async def health_check() -> dict:
    return {"is_running": True}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0")
