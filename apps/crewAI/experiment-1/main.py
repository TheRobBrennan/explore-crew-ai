from tools.load_environment_variables import load_env_variables
from crew.create_crew import run_crew

def main():
    # Load our OpenAI API key and other environment variables from the .env file
    load_env_variables()

    # Run the crew
    run_crew()

if __name__ == "__main__": # pragma: no cover
    main()
