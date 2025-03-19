from apscheduler.schedulers.background import BackgroundScheduler
from fastapi import FastAPI
from contextlib import asynccontextmanager
from importer.importer import import_prices, import_products
from routes.product_routes import router as product_router
from routes.price_routes import router as price_router
import logging

logging.basicConfig(level=logging.INFO)
scheduler = BackgroundScheduler()

def job():
    logging.info("test")
@asynccontextmanager
async def lifespan(app: FastAPI):

    logging.info("Starting up the application...")

    scheduler.add_job(import_prices, 'cron', hour=1, minute=0)  # runs every day at midnight
    scheduler.add_job(import_products, 'cron', hour=2, minute=0)  # runs every day at midnight
    # scheduler.add_job(job, 'interval', minutes=1)

    scheduler.start()
    logging.info("Scheduler started with 2 tasks.")

    yield

    logging.info("Shutting down the application...")
    scheduler.shutdown()
    logging.info("Scheduler shutdown completed.")

app = FastAPI(lifespan=lifespan)

# Include your routes
app.include_router(product_router)
app.include_router(price_router)
