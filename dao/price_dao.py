import logging

import psycopg2
from psycopg2.extras import execute_values

from dao.connection import get_connection

logging.basicConfig(level=logging.INFO)

def get_prices_by_product_id(product_id):

    # 2. Connect to PostgreSQL
    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cursor:
                query = """
                    SELECT * FROM price WHERE product_id = %s
                """
                cursor.execute(query, (product_id,))
                prices = cursor.fetchall()
                if prices is None or len(prices) == 0:
                    return None

                return prices

    except psycopg2.Error as e:
        logging.ERROR("Error while getting last sync date:", e)
    finally:
        conn.close()

def instertProductPrices(product_pricess):

        prices = [(p.get('id'), p.get('price'), p.get('discountedPrice')) for p in product_pricess]

        # 2. Connect to PostgreSQL
        conn = get_connection()

        try:
            with conn:
                with conn.cursor() as cursor:

                    sql = """
                        INSERT INTO public.price (product_id, price, discount_price)
                        VALUES %s
                    """

                    # This packs all records into a single multi-row INSERT
                    execute_values(cursor, sql, prices)
        except psycopg2.Error as e:
            logging.ERROR("Error: in instert product prices ", e)
        finally:
            conn.close()

def instertProduct(products):

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

