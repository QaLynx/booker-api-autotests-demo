from pydantic import BaseModel, RootModel
from typing import List

class BookingItem(BaseModel):
    bookingid: int

class AllBookingResponse(BaseModel):
    bookings: List[BookingItem]

