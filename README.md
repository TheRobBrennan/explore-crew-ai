# Welcome

This project explores working with [Python](https://www.python.org/) and [CrewAI](https://www.crewai.com/) to assemble a crew of AI agents—powered by large language models (LLMs) such as OpenAI ChatGPT 4—to work together and achieve a common goal.

**IMPORTANT: Using OpenAI will incur actual costs when running this code.**

For example, a single run of the `create-business-plan` example cost me **$0.79**.

For more details, please see the [OpenAI Developer Documentation](https://platform.openai.com/docs/overview).

## Getting started

Our first (and so far only) example uses CrewAI to orchestrate three agents - a business consultant, a market research analyst, and a technologist - to work together on evaluating an idea for a startup company and generating a business plan.

This example was inspired by [Maya Akim](https://www.youtube.com/@maya-akim)'s video - [How I Made AI Assistants Do My Work For Me: CrewAI](https://www.youtube.com/watch?v=kJvXT25LkwA) - and significantly enhanced to reflect my tastes in implementing a modular design that is validated with unit tests.

Please copy `apps/create-business-plan/.env.sample` to `apps/create-business-plan/.env` so you can supply a valid OpenAI API key and any other desired environment variables.

Once you've done that, let's take a look at the project-specific [README](./apps/create-business-plan/README.md)

## Additional resources

If you would like to dive into advanced ways you can work with this project, please see [DEVELOP.md](./DEVELOP.md)

If you are getting your feet wet exploring Python and local development, please feel free to take a look at the [PYTHON_CHEATSHEET](./PYTHON_CHEATSHEET.md).
