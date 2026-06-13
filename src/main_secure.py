import hashlib
import requests
import subprocess
import sys

URL = "http://localhost:8000/update.py"

EXPECTED_HASH = "99c7825809f1ae3ad50a123ec6bd8b7a9c79d04b7cfcc2f6bdbf4d966d0dd344"

response = requests.get(URL)
response.raise_for_status()

actual_hash = hashlib.sha256(response.content).hexdigest()

if actual_hash != EXPECTED_HASH:
    print("Integrity check failed!")
    print(f"Expected: {EXPECTED_HASH}")
    print(f"Actual:   {actual_hash}")
    sys.exit(1)

with open("update.py", "wb") as f:
    f.write(response.content)

print("Downloaded update.py")

print("Executing update")

subprocess.run(["python", "update.py"])
