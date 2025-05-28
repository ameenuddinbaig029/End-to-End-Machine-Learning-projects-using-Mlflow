"""
🧠 Purpose of this script:
This logging setup is used to create and manage log files for your machine learning project, so that all key events (like data loading, training, errors) are recorded.

1. ✅ Why we use logging:
   Logging helps track what's happening inside our code — useful for debugging, performance monitoring, and reproducing results.

2. 📈 Benefit of using a custom logger:
   - Logs are saved to a file (`running_logs.log`) for later inspection.
   - Logs are also shown in the console during runtime.
   - Helps identify when, where, and what happened in the code.

3. ❌ Problem before using it:
   Without logging, we had to rely on `print()` statements, which don't give timestamps, log levels, or structured diagnostics. Also, prints disappear once the terminal is closed.

4. 🛠️ How this fixes it:
   This script:
   - Creates a `logs/` directory (if not exists).
   - Saves logs to `running_logs.log`.
   - Prints logs to console as well.
   - Uses structured formatting with time, severity level, and module name.
"""

import os
import sys
import logging

# Define a standard log message format
logging_str = "[%(asctime)s: %(levelname)s:%(module)s:%(message)s]"

# Directory and file path where logs will be saved
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")

# Create logs directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Configure the logging system
logging.basicConfig(
    level=logging.INFO,               # Log messages at INFO level or higher
    format=logging_str,              # Use the custom format defined above
    handlers=[
        logging.FileHandler(log_filepath),     # Save logs to file
        logging.StreamHandler(sys.stdout)      # Print logs to console
    ]
)

# Create a logger instance with a custom name
logger = logging.getLogger("mlProjectLogger")
