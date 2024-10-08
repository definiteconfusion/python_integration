import subprocess
import datetime

def binary():
    start = datetime.datetime.now()
    subprocess.run(
        ['python3', 'mainRs.py'],
        capture_output=True,
        text=True
    ).stdout
    return datetime.datetime.now() - start

def native():
    start = datetime.datetime.now()
    subprocess.run(
        ['python3', 'main.py'],
        capture_output=True,
        text=True
    ).stdout
    return datetime.datetime.now() - start

print(binary() / native())