import psycopg2
from psycopg2 import Error
from psycopg2.extensions import AsIs
from psycopg2 import sql
import datetime
import requests
import config
# datetime.date.today().strftime("%d-%m-%Y")
# for DB date

def get_current_state(user_id):
    try:
        connection = psycopg2.connect(user="postgres",
                                              password="12345678",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="postgres")
        cursor = connection.cursor()
        some_articul = f'''SELECT status
        FROM weather_bot_status
        WHERE user_id = '{user_id}'
        ;'''
        cursor.execute(some_articul)
        records = cursor.fetchone()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            if records is not None:
                return records[0]
            else:
                return config.States.S_START.value

def set_state(user_id, state_val):
    try:
        connection = psycopg2.connect(user="postgres",
                                              password="12345678",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="postgres")
        cursor = connection.cursor()


        some_articul = f'''INSERT INTO  weather_bot_status (user_id, status)
        VALUES ('{user_id}'::text, '{state_val}'::text) 
        ON CONFLICT(user_id) DO UPDATE SET status = EXCLUDED.status
        ;'''
        cursor.execute(some_articul)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return  False
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            return  True

def set_info(user_id, user_msg, state_val):
    try:
        connection = psycopg2.connect(user="postgres",
                                              password="12345678",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="postgres")
        cursor = connection.cursor()

        # INSERT
        # INTO
        # public.weather_user_info(
        #     user_id, text_msg, date_msg, status)
        # VALUES(985773281, 'noname', '2023-01-01'::Date, 1);

        some_articul = f'''INSERT INTO  weather_user_info  (user_id, text_msg, date_msg, status)
        VALUES ('{user_id}'::text, '{user_msg}'::text, now(), '{state_val}'::text) 
        ON CONFLICT(user_id, date_msg) DO UPDATE SET text_msg = EXCLUDED.text_msg
        ;'''
        cursor.execute(some_articul)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return  False
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            return  True

def get_current_info(user_id, status, limit = 1):
    try:
        connection = psycopg2.connect(user="postgres",
                                              password="12345678",
                                              host="127.0.0.1",
                                              port="5432",
                                              database="postgres")
        cursor = connection.cursor()
        some_articul = f'''
        SELECT text_msg FROM public.weather_user_info
        WHERE status = '{status}'
        ORDER BY date_msg DESC 
        LIMIT {limit}
        ;'''
        cursor.execute(some_articul)
        records = cursor.fetchone()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            if records is not None:
                return records[0]
            else:
                return config.States.S_START.value

set_info("985773281","xave nota name","3")

print(get_current_info(985773281, 3))