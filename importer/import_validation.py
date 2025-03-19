import datetime
from dao.import_dao import get_last_import_datetime

def validate_import_prices_date() -> bool:

    last_import_date_time = get_last_import_datetime()

    # If no sync date exists, we allow syncing.
    if last_import_date_time is None:
        return True

    # Convert datetime to date only.
    last_import_date = last_import_date_time.date()

    # If the last sync date is today or later, do not sync.
    if last_import_date >= datetime.date.today():
        return  False

    return True
