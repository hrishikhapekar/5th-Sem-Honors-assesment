import subprocess
import sys

# Run app in background
process = subprocess.Popen([sys.executable, "app.py"])
print(f"Service started with PID: {process.pid}")
print("Service Status: RUNNING")