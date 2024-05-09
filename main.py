from config import get_configuration
from scheduler import start_scheduler
import logging


def main():
    source, replica, log_path, interval = get_configuration()
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler(log_path),
                                  logging.StreamHandler()])
    start_scheduler(source, replica, interval)


if __name__ == "__main__":
    main()
