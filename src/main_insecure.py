import requests
import subprocess

URL = "http://localhost:8000/update.py"

response = requests.get(URL)
response.raise_for_status()

with open("update.py", "wb") as f:
    f.write(response.content)

print("Downloaded update.py")

print("Executing update")

subprocess.run(["python", "update.py"])
