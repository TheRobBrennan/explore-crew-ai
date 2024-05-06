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
    goal="Find out how big the demand is for my products and suggest how to reach the widest possible customer base.",

    # Backstory of the agent
    backstory="""You are an expert at understanding the market demand, target audience, and competition. This is crucial for 
		validating whether an idea fulfills a market need and has the potential to attract a wide audience. You are good at coming up
		with ideas on how to appeal to widest possible audience.
		""",

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
    goal="Make an assessment on how technologically feasable the company is, and what type of technologies the company needs to adopt in order to succeed.",

    # Backstory of the agent
    backstory="""You are a visionary in the realm of technology, with a deep understanding of both current and emerging technological trends. Your 
		expertise lies not just in knowing the technology but in foreseeing how it can be leveraged to solve real-world problems and drive business innovation.
		You have a knack for identifying which technological solutions best fit different business models and needs, ensuring that companies stay ahead of 
		the curve. Your insights are crucial in aligning technology with business strategies, ensuring that the technological adoption not only enhances 
		operational efficiency but also provides a competitive edge in the market.""",
    
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
    goal="Evaluate and advise on the business model, scalability, and potential revenue streams to ensure long-term sustainability and profitability",

    # Backstory of the agent
    backstory="""You are a seasoned professional with expertise in shaping business strategies. Your insight is essential for turning innovative ideas 
		into viable business models. You have a keen understanding of various industries and are adept at identifying and developing potential revenue streams. 
		Your experience in scalability ensures that a business can grow without compromising its values or operational efficiency. Your advice is not just
		about immediate gains but about building a resilient and adaptable business that can thrive in a changing market.""",

    # Display verbose output
    verbose=True,

    # Enable collaboration with other agents
    allow_delegation=True,
)

# Define tasks for our agents to run
task1 = Task(
    description="""Analyze what the market demand for plugs for holes in crocs (shoes) so that this iconic footware looks less like swiss cheese. 
		Write a detailed report with description of what the ideal customer might look like, and how to reach the widest possible audience. The report has to 
		be concise with at least 10 bullet points and it has to address the most important areas when it comes to marketing this type of business.
    """,
    agent=market_research_analyst,
)

task2 = Task(
    description="""Analyze how to produce plugs for crocs (shoes) so that this iconic footware looks less like swiss cheese.. Write a detailed report 
		with description of which technologies the business needs to use in order to make High Quality T shirts. The report has to be concise with 
		at least 10  bullet points and it has to address the most important areas when it comes to manufacturing this type of business. 
    """,
    agent=technologist,
)

task3 = Task(
    description="""Analyze and summarize marketing and technological report and write a detailed business plan with 
		description of how to make a sustainable and profitable "plugs for crocs (shoes) so that this iconic footware looks less like swiss cheese" business. 
		The business plan has to be concise with 
		at least 10  bullet points, 5 goals and it has to contain a time schedule for which goal should be achieved and when.
    """,
    agent=business_consultant,
)

def hello():
    return f"\nEXAMPLE: Sequentially run three agents to evaluate an idea for a business startup and generate a business plan.\n"

if __name__ == "__main__":
    print(hello())

