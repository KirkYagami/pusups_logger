from dotenv import load_dotenv
import subprocess

load_dotenv(override=True)

# Define the command and its arguments
command = ["flask", "run"]
result = subprocess.run(command)


print("Flask server started successfully.")
print("STDOUT:")
print(result.stdout)