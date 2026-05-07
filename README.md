# 🏍️ BikeZang — Python Backend

FastAPI backend for the BikeZang bike service booking platform.

## Flow
```
Customer fills form → Submit →
Backend saves to Supabase → Returns WhatsApp link →
Frontend opens WhatsApp with booking details sent to YOUR number
```

## Project Structure
```
bikezang/
├── frontend/
│   └── index.html           # HTML form
├── models/
│   ├── __init__.py
│   └── schemas.py           # Request/response models
├── routes/
│   ├── __init__.py
│   ├── booking.py           # /api/booking/create & /all
│   └── otp.py               # OTP routes
├── services/
│   ├── __init__.py
│   ├── booking_service.py   # Supabase CRUD
│   └── whatsapp_service.py  # Builds WhatsApp URL
├── main.py                  # FastAPI app
├── config.py                # Env settings
├── requirements.txt
├── render.yaml              # Deployment config
├── supabase_schema.sql      # Run once in Supabase
├── README.md
└── .env.example             # Copy → .env and fill keys
```

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure .env
```bash
cp .env.example .env
# Fill in your keys
```

### 3. Setup Supabase
- Create free project at https://supabase.com
- Run `supabase_schema.sql` in SQL Editor
- Copy URL + anon key to `.env`

### 4. Add your WhatsApp number
```env
WHATSAPP_BUSINESS_NUMBER=919876543210
```

### 5. Run
```bash
uvicorn main:app --reload
```

API docs: http://localhost:8000/docs

### 6. Update Imports (after reorganization)
Your code should now use:
```python
from models.schemas import BookingRequest
from routes.booking import router as booking_router
from services.booking_service import save_booking
from services.whatsapp_service import build_whatsapp_url
```

## API Endpoints

| Method | Endpoint | What it does |
|--------|----------|--------------|
| POST | `/api/booking/create` | Save booking + return WhatsApp URL |
| GET  | `/api/booking/all` | List all bookings (admin) |