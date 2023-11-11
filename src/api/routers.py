from fastapi import APIRouter

new_router = APIRouter(tags=["new"])


@new_router.get("")
async def get_new():
    return "new"
