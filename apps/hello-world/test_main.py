# apps/hello-world/test_main.py

import subprocess

def test_hello_world():
    result = subprocess.run(["python3", "main.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, world!"
