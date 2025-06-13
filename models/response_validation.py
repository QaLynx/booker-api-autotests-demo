from pydantic import BaseModel
from typing import List

class BookingItem(BaseModel):
    bookingid: int

class AllBookingResponse(BaseModel):
    __root__: List[BookingItem]

