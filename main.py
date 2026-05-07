from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import booking

app = FastAPI(title="BikeZang API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(booking.router, prefix="/api/booking", tags=["Booking"])

@app.get("/")
def root():
    return {"message": "BikeZang API running 🏍️"}
