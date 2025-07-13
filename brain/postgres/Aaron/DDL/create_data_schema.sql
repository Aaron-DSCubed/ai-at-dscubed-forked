CREATE SCHEMA IF NOT EXISTS project_two;

CREATE TABLE IF NOT EXISTS project_two.spotify_top_artists (
    artist_id SERIAL PRIMARY KEY,
    artist_name TEXT NOT NULL,
    monthly_listeners_millions DECIMAL(5,2),
    genre TEXT,
    country TEXT,
    global_rank INTEGER CHECK (global_rank BETWEEN 1 AND 100),
    is_active BOOLEAN DEFAULT TRUE
);