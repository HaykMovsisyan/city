import logging

import psycopg2
from psycopg2.extras import execute_values

from dao.connection import get_connection


def get_last_import_datetime():

    # 2. Connect to PostgreSQL
    conn = get_connection()

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT timestamp FROM price ORDER BY id DESC LIMIT 1;")
            rows = cursor.fetchall()
            if rows is None or len(rows) == 0:
                return None

            return rows[0][0]
    except psycopg2.Error as e:
        logging.ERROR("Error while getting last sync date:", e)
    finally:
        if conn:
            conn.close()

def instert_product(products):

    records = [(p.get('id'), p.get('name'), p.get('category_name'), p.get('photo_url')) for p in products]

    # 2. Connect to PostgreSQL
    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cursor:
                sql = """
                    INSERT INTO public.product (id, name, category_name, photo_url)
                    VALUES %s
                    ON CONFLICT (id) DO UPDATE SET
                        name = EXCLUDED.name,
                        category_name = EXCLUDED.category_name,
                        photo_url = EXCLUDED.photo_url;
                    """

                # This packs all records into a single multi-row INSERT
                execute_values(cursor, sql, records)
    except psycopg2.Error as e:
        logging.ERROR("Error in instert product:", e)
    finally:
        conn.close()

