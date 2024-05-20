from crewai import Task

# Multiline constants for task description and expected output
DESCRIPTION = """
    Analyze and summarize marketing and technological reports and write a detailed business plan describing how to make sustainable and profitable 
    "plugs for Crocs (shoes) so that this iconic footwear looks less like Swiss cheese" business. 
    
    The business plan has to be concise with at least ten bullet points and five goals and must contain 
    a schedule for which goals should be achieved and when starting no earlier than mid-May 2024.
"""

EXPECTED_OUTPUT = """
    A detailed business plan that integrates the marketing and technological reports, outlining a sustainable and profitable business model for the product.
"""

def create_business_plan_task(agent):
    return Task(
        description=DESCRIPTION,
        agent=agent,
        expected_output=EXPECTED_OUTPUT
    )
