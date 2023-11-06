from typing import Annotated

from fastapi import APIRouter, Query
from pydantic import BaseModel

from src.db import hotels

booking_router = APIRouter()


class SHotelInput(BaseModel):
    title: Annotated[str, Query(max_length=20, min_length=2)]
    stars: Annotated[int, Query(ge=1, le=5)]


@booking_router.get("/hotels")
async def list_hotels() -> dict:
    return hotels


@booking_router.post("/hotels", status_code=201)
async def add_hotel(hotel_data: SHotelInput) -> dict:
    hotels[hotel_data.title] = hotel_data.stars
    return hotels
