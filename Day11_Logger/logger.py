import logging
from datetime import datetime

# Configure logging system
logging.basicConfig(
    filename="events.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_event(message):
    logging.info(message)
    print("Logged:", message)

# Example usage
log_event("Program started.")
log_event("User logged in.")
log_event("Data processed successfully.")
log_event("Program finished.")
