import os

from crewai import Agent, Task, Process, Crew
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Agent: Market Research Analyst
market_research_analyst = Agent(
    # Role of the agent
    role="Market Research Analyst",

    # Goal of the agent
    goal="Find out how much demand there is for my products and suggest ways to reach the widest possible customer base.",

    # Backstory of the agent
    backstory="""
        You are an expert at understanding market demand, target audience, and competition. This is crucial for validating 
        whether an idea fulfills a market need and has the potential to attract a wide audience. 
            
        You are also good at developing ideas that appeal to the broadest possible audience.""",

    # Display verbose output
    verbose=True,

    # Enable collaboration with other agents
    allow_delegation=True,
)

# Agent: Technologist
technologist = Agent(
    # Role of the agent
    role="Technology Expert",

    # Goal of the agent
    goal="Identify the best technologies and processes to use to create our products and services.",

    # Backstory of the agent
    backstory="""
        You are a visionary in the realm of technology, with a deep understanding of current and emerging technological trends. 
        Your expertise lies in knowing the technology and foreseeing how it can be leveraged to solve real-world problems and drive 
        business innovation. You have a knack for identifying which technological solutions best fit different business models and needs, 
        ensuring that companies stay ahead of the curve. Your insights are crucial in aligning technology with business strategies, 
        ensuring that technological adoption enhances operational efficiency and provides a competitive edge in the market.
    """,
    
    # Display verbose output
    verbose=True,

    # Enable collaboration with other agents
    allow_delegation=True,
)

# Agent: Business Development Consultant
business_consultant = Agent(
    # Role of the agent
    role="Business Development Consultant",

    # Goal of the agent
    goal="Evaluate and advise on the business model, scalability, and potential revenue streams to ensure long-term sustainability and profitability.",

    # Backstory of the agent
    backstory="""
        You are a seasoned professional with expertise in shaping business strategies. Your insight is essential for turning innovative ideas into viable 
        business models. You have a keen understanding of various industries and are adept at identifying and developing potential revenue streams. 
        Your experience in scalability ensures that a business can grow without compromising its values or operational efficiency. Your advice is not just
        about immediate gains but building a resilient and adaptable business that can thrive in a changing market.
    """,

    # Display verbose output
    verbose=True,

    # Enable collaboration with other agents
    allow_delegation=True,
)

# Define tasks for our agents to run
task1 = Task(
    description="""
        Analyze the market demand for plugs for holes in Crocs (shoes) so that this iconic footwear looks less like Swiss cheese. 
        Write a detailed report describing the ideal customer and how to reach the broadest possible audience. The report has to be concise, 
        with at least ten bullet points, and address the most critical areas when marketing this type of business.
    """,

    # The agent responsible for executing this task
    agent=market_research_analyst,

    # Expected output
    expected_output="""
        A detailed report outlining the market demand for the product, the ideal customer profile, and a marketing strategy to reach the broadest possible audience.        
    """

)

task2 = Task(
    description="""
        Analyze how to produce plugs for Crocs (shoes) so that this iconic footwear looks less like Swiss cheese. 
        Write a detailed report describing which technologies the business needs to use to make High-Quality T-shirts. 
        The report has to be concise with at least ten bullet points and address the most critical areas when manufacturing this type of business. 
    """,

    # The agent responsible for executing this task
    agent=technologist,

    # Expected output
    expected_output="""
        A detailed report outlines the business' technological requirements, including the type of technologies needed to produce the product.
    """,    
)

task3 = Task(
    description="""
        Analyze and summarize marketing and technological reports and write a detailed business plan describing how to make sustainable and profitable 
        "plugs for Crocs (shoes) so that this iconic footwear looks less like Swiss cheese" business. 
        
        The business plan has to be concise with at least ten bullet points and five goals and must contain 
        a schedule for which goals should be achieved and when starting no earlier than mid-May 2024.
    """,

    # The agent responsible for executing this task
    agent=business_consultant,

    # Expected output
    expected_output="""
        A detailed business plan that integrates the marketing and technological reports, outlining a sustainable and profitable business model for the product.
    """
)

# Create a crew of agents and tasks
crew = Crew(
    # Define the agents and tasks for the crew
    agents=[market_research_analyst, technologist, business_consultant],
    tasks=[task1, task2, task3],

    # Verbose output
    verbose=2,

    # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into the next task
    process=Process.sequential, 
)

def run():
    result = crew.kickoff()
    print(f"\nThe crew has completed their tasks:\n\n{result}")

if __name__ == "__main__":
    run()

