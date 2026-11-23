
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_file():
    print(f"{threading.current_thread().name}: Downloading file...")
    time.sleep(2)
    print("File downloaded successfully!")

def process_data():
    print(f"{threading.current_thread().name}: Processing data...")
    time.sleep(3)
    print("Data processing completed!")

def send_email():
    print(f"{threading.current_thread().name}: Sending email...")
    time.sleep(1)
    print("Email sent successfully!")

def backup_files():
    print(f"{threading.current_thread().name}: Backing up files...")
    time.sleep(2)
    print("Backup completed!")

def main():
    tasks = [
        download_file,
        process_data,
        send_email,
        backup_files
    ]

    print("Starting multiple threads...\n")

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(task) for task in tasks]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as error:
                print("Task failed:", error)

    print("\nAll tasks completed successfully!")

if __name__ == "__main__":
    main()
