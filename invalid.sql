CREATE TABLE IF NOT EXISTS public.weather_user_info
(
    user_id text COLLATE pg_catalog."default" NOT NULL,
    text_msg text COLLATE pg_catalog."default",
    date_msg timestamp without time zone NOT NULL,
    status text COLLATE pg_catalog."default" NOT NULL DEFAULT '0'::text,
    CONSTRAINT user_info_pkey PRIMARY KEY (user_id, date_msg),
    CONSTRAINT fk_user_id FOREIGN KEY (user_id)
        REFERENCES public.weather_bot_status (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.weather_user_info
    OWNER to postgres;