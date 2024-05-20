from crewai import Task

# Multiline constants for task description and expected output
DESCRIPTION = """
    Analyze how to produce plugs for Crocs (shoes) so that this iconic footwear looks less like Swiss cheese. 
    Write a detailed report describing which technologies the business needs to use to make High-Quality T-shirts. 
    The report has to be concise with at least ten bullet points and address the most critical areas when manufacturing this type of business.
"""

EXPECTED_OUTPUT = """
    A detailed report outlines the business' technological requirements, including the type of technologies needed to produce the product.
"""

def create_analyze_technology_requirements_task(agent):
    return Task(
        description=DESCRIPTION,
        agent=agent,
        expected_output=EXPECTED_OUTPUT
    )
