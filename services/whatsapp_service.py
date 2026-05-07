from config import settings
import urllib.parse

def build_whatsapp_url(booking: dict) -> str:
    """
    Builds a wa.me link that sends the booking details
    directly to YOUR WhatsApp business number.
    The customer clicks this and it opens WhatsApp with
    all their booking info pre-filled as a message to you.
    """
    notes_line = f"\n📝 Notes: {booking['notes']}" if booking.get('notes') else ""

    message = (
        f"🏍️ *New Bike Service Booking*\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"👤 Name: {booking['customer_name']}\n"
        f"📞 Phone: {booking['phone']}\n"
        f"🔧 Service: {booking['service_type']}\n"
        f"🏍️ Bike: {booking['bike_brand']} {booking['bike_model']}\n"
        f"📅 Date: {booking['preferred_date']}\n"
        f"⏰ Time: {booking['preferred_time']}\n"
        f"📍 Address: {booking['location']}"
        f"{notes_line}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🆔 Booking ID: {booking['booking_id']}"
    )

    encoded = urllib.parse.quote(message)
    return f"https://wa.me/{settings.WHATSAPP_BUSINESS_NUMBER}?text={encoded}"
