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
        some_articul = f'''SELECT status_client_dilog 
        FROM echo_bot_status
        WHERE united_id = '{user_id}'
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


        some_articul = f'''INSERT INTO  echo_bot_status (united_id, status_client_dilog)
        VALUES ('{user_id}'::text, '{state_val}'::text) 
        ON CONFLICT(united_id) DO UPDATE SET status_client_dilog = EXCLUDED.status_client_dilog
        ;'''
        cursor.execute(some_articul)
        connection.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return False
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            return True

