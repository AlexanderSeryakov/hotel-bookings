from fastapi import FastAPI

from booking_router import booking_router

app = FastAPI(title="Online-booking")

app.include_router(booking_router, prefix="/booking")


@app.get("/")
async def health_check() -> dict:
    return {"is_running": True}
