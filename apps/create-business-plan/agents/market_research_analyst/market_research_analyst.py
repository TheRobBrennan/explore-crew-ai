from crewai import Agent

# Use multiline constants for defining our agent
ROLE = """
    Market Research Analyst
"""

GOAL = """
    Find out how much demand there is for my products and suggest ways to reach the widest possible customer base.
"""

BACKSTORY = """
    You are an expert at understanding market demand, target audience, and competition. This is crucial for validating 
    whether an idea fulfills a market need and has the potential to attract a wide audience. 
    You are also good at developing ideas that appeal to the broadest possible audience.
"""

# Agent: Market Research Analyst
def create_market_research_analyst():
    return Agent(
        role=ROLE.strip(),
        goal=GOAL.strip(),
        backstory=BACKSTORY.strip(),
        verbose=True,
        allow_delegation=True,
    )
