import pytest
import subprocess
from hello_world import hello

def test_hello():
    assert hello() == "Hello, world!"

def test_script_execution():
    # Execute the script and capture the output to test
    # if __name__ == "__main__": ...
    # by capturing the script output and setting text to True so we are capturing the output as a string instead of bytes
    result = subprocess.run(['python3', 'hello_world.py'], capture_output=True, text=True)
    
    # Check if the output matches the expected output
    assert result.stdout == "Hello, world!\n"
