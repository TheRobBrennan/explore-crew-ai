from crewai import Task

# Multiline constants for task description and expected output
DESCRIPTION = """
    Analyze the market demand for plugs for holes in Crocs (shoes) so that this iconic footwear looks less like Swiss cheese. 
    Write a detailed report describing the ideal customer and how to reach the broadest possible audience. The report has to be concise, 
    with at least ten bullet points, and address the most critical areas when marketing this type of business.
"""

EXPECTED_OUTPUT = """
    A detailed report outlining the market demand for the product, the ideal customer profile, and a marketing strategy to reach the broadest possible audience.        
"""

def create_analyze_market_demand_task(agent):
    return Task(
        description=DESCRIPTION,
        agent=agent,
        expected_output=EXPECTED_OUTPUT
    )
