-- Table: public.weather_bot_status

-- DROP TABLE IF EXISTS public.weather_bot_status;

CREATE TABLE IF NOT EXISTS public.weather_bot_status
(
    user_id text COLLATE pg_catalog."default" NOT NULL,
    status text COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT echo_bot_status_pkey PRIMARY KEY (user_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.weather_bot_status
    OWNER to postgres;