from fastapi import APIRouter, HTTPException
from models.schemas import BookingCreate, BookingResponse
from services.booking_service import create_booking, get_all_bookings
from services.whatsapp_service import build_whatsapp_url

router = APIRouter()

@router.post("/create", response_model=BookingResponse)
async def create_new_booking(booking: BookingCreate):
    result = await create_booking(booking)

    if not result["success"]:
        raise HTTPException(status_code=500, detail="Failed to save booking")

    # Build WhatsApp URL pointing to YOUR business number
    wa_url = build_whatsapp_url(result["data"])
    print(f"[WhatsApp] {wa_url}")  # Also logged in terminal

    return BookingResponse(
        success=True,
        booking_id=result["booking_id"],
        message=wa_url   # Frontend uses this URL to open WhatsApp
    )

@router.get("/all")
async def list_bookings():
    """Admin: view all bookings"""
    return await get_all_bookings()
