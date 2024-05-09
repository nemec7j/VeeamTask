import os


def get_path_input(prompt, is_file=False):
    while True:
        path = input(prompt)
        if is_file:
            if not os.path.exists(os.path.dirname(path)):
                print("The directory for this path does not exist. Please try again.")
            elif os.path.isdir(path):
                print("A directory path was provided where a file path is expected. Please try again.")
            else:
                return path
        else:
            if not os.path.isdir(path):
                print("The specified path does not exist or is not a directory. Please try again.")
            else:
                return path


def get_interval_input(prompt, default=60):
    while True:
        interval_input = input(prompt)
        try:
            interval = int(interval_input or default)
            if interval <= 0:
                raise ValueError
            return interval
        except ValueError:
            print("Invalid synchronization interval. Please enter a positive integer.")


def get_configuration():
    source = get_path_input("Enter the path to the source folder: ")
    replica = get_path_input("Enter the path to the replica folder: ")
    log_path = get_path_input("Enter the full path for the log file (including the filename, e.g., log.txt): ",
                              is_file=True)
    interval = get_interval_input("Enter the synchronization interval in seconds (default 60): ")
    return source, replica, log_path, interval
