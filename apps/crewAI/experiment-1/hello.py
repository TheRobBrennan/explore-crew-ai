from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

def hello():
    return f"\nHello from experiment 1 - {openai_api_key}\n"

if __name__ == "__main__":
    print(hello())
