# apps/hello-world/test_main.py

from main import hello_world

def test_hello_world():
    assert hello_world() == "Hello, world!"

