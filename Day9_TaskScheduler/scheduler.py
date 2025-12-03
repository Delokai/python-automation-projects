import schedule
import time

def job():
    print("Running scheduled task...")

# Run the job every 10 seconds
schedule.every(10).seconds.do(job)

print("Scheduler started. Press CTRL + C to stop.\n")

while True:
    schedule.run_pending()
    time.sleep(1)
