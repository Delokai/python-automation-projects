🕒 Day 9 — Task Scheduler Automation

This script runs a task automatically on a timer using the schedule library.
It's useful for automated reporting, reminders, scraping, backups, and more.

🔧 Tools Used

schedule — simple Python scheduling library

time — used for delays between checks

Python 3

📌 What the Script Does

Defines a function: job()

Runs it every 10 seconds

Loops forever until manually stopped

▶️ How to Run

Install dependencies:

py -m pip install schedule


Run the script:

python scheduler.py


Stop it using:

CTRL + C

📘 Example Output
Scheduler started. Press CTRL + C to stop.

Running scheduled task...
Running scheduled task...
Running scheduled task...

🎯 Skills Learned

Task automation

Timers and intervals

Scheduling jobs

Writing background scripts

Real-world automation patterns
