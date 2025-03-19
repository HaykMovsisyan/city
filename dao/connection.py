import logging
import os

import psycopg2
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

# Load environment variables from .env file
load_dotenv()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

def get_connection():

    try:
        return psycopg2.connect(
            host=HOST,
            port=PORT,
            dbname=DATABASE,
            user=USERNAME,
            password=PASSWORD
        )
        # psycopg2.connect(
        #     host="localhost",
        #     port="5432",
        #     database="city",
        #     user="postgres",
        #     password="secretpassword",
        # )

    except psycopg2.Error as e:
        logging.ERROR("Error in getting connection.py", e)