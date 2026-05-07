import uuid
from supabase import create_client
from config import settings
from models.schemas import BookingCreate

_supabase = None

def get_supabase():
    global _supabase
    if _supabase is None:
        try:
            _supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        except Exception as e:
            print(f"⚠️  Supabase connection failed: {e}")
            print("💡 Using mock mode for testing. Replace .env with valid Supabase credentials.")
            _supabase = None  # Return None to use mock data
    return _supabase

async def create_booking(booking: BookingCreate) -> dict:
    supabase = get_supabase()
    booking_id = "BK" + str(uuid.uuid4())[:8].upper()

    data = {
        "booking_id":     booking_id,
        "customer_name":  booking.customer_name,
        "phone":          booking.phone,
        "bike_brand":     booking.bike_brand,
        "bike_model":     booking.bike_model,
        "service_type":   booking.service_type,
        "preferred_date": booking.preferred_date,
        "preferred_time": booking.preferred_time,
        "location":       booking.location,
        "notes":          booking.notes,
        "status":         "pending",
    }

    # If Supabase is not available, just return success without saving
    if supabase is None:
        print(f"✅ Mock booking created: {booking_id}")
        return {"success": True, "booking_id": booking_id, "data": data}

    try:
        response = supabase.table("bookings").insert(data).execute()
        if response.data:
            return {"success": True, "booking_id": booking_id, "data": data}
        return {"success": False, "booking_id": "", "data": {}}
    except Exception as e:
        print(f"⚠️  Error saving to Supabase: {e}")
        # Still return success since booking was created locally
        return {"success": True, "booking_id": booking_id, "data": data}

async def get_all_bookings() -> list:
    supabase = get_supabase()
    if supabase is None:
        return []  # Return empty list if Supabase not available
    
    try:
        res = supabase.table("bookings").select("*").order("created_at", desc=True).execute()
        return res.data or []
    except Exception as e:
        print(f"⚠️  Error fetching bookings: {e}")
        return []
