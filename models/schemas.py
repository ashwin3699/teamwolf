from pydantic import BaseModel
from typing import Optional

class BookingCreate(BaseModel):
    customer_name: str
    phone: str
    bike_brand: str
    bike_model: str
    service_type: str
    preferred_date: str
    preferred_time: str
    location: str
    notes: Optional[str] = ""

class BookingResponse(BaseModel):
    success: bool
    booking_id: str
    message: str
