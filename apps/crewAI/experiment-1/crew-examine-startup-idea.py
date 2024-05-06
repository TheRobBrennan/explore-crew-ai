import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def hello():
    return f"\nEXAMPLE: Sequentially run three agents to evaluate an idea for a business startup and generate a business plan.\n"

if __name__ == "__main__":
    print(hello())

