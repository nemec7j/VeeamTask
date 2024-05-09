import schedule
import time
from sync import sync_folders


def start_scheduler(source, replica, interval):
    schedule.every(interval).seconds.do(sync_folders, source, replica)
    while True:
        schedule.run_pending()
        time.sleep(1)
