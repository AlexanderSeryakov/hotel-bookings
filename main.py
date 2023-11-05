from fastapi import FastAPI


app = FastAPI(title="Online-booking")


@app.get("/")
async def healthcheck():
    return {"ok": True}
