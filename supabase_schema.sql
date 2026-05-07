-- Run this once in your Supabase SQL Editor
-- supabase.com → Your Project → SQL Editor → New Query

CREATE TABLE bookings (
    id               SERIAL PRIMARY KEY,
    booking_id       VARCHAR(20) UNIQUE NOT NULL,
    customer_name    VARCHAR(100) NOT NULL,
    phone            VARCHAR(15) NOT NULL,
    bike_brand       VARCHAR(50) NOT NULL,
    bike_model       VARCHAR(50) NOT NULL,
    service_type     VARCHAR(100) NOT NULL,
    preferred_date   VARCHAR(20) NOT NULL,
    preferred_time   VARCHAR(30) NOT NULL,
    location         TEXT NOT NULL,
    notes            TEXT DEFAULT '',
    status           VARCHAR(20) DEFAULT 'pending',
    created_at       TIMESTAMP DEFAULT NOW()
);

-- Enable Row Level Security
ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;

-- Allow all for now (lock down in production)
CREATE POLICY "Allow all" ON bookings FOR ALL USING (true);
