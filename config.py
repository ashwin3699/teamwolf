from pydantic import root_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # WhatsApp Business Number (your number with country code, no +)
    # Example: 919876543210
    WHATSAPP_BUSINESS_NUMBER: str = "91XXXXXXXXXX"

    # Supabase
    SUPABASE_URL: str = ""
    SUPABASE_KEY: str = ""

    @root_validator(pre=True)
    def normalize_whatsapp_number(cls, values):
        if not values.get("WHATSAPP_BUSINESS_NUMBER"):
            values["WHATSAPP_BUSINESS_NUMBER"] = values.get("WHATSAPP_NUMBER", "")
        return values

    class Config:
        env_file = ".env"

settings = Settings()
