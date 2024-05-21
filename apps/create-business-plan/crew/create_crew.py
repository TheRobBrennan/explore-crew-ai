from crewai import Crew, Process
from agents.market_research_analyst.market_research_analyst import create_market_research_analyst
from agents.technologist.technologist import create_technologist
from agents.business_consultant.business_consultant import create_business_consultant
from tasks.analyze_market_demand.analyze_market_demand import create_analyze_market_demand_task
from tasks.analyze_technology_requirements.analyze_technology_requirements import create_analyze_technology_requirements_task
from tasks.create_business_plan.create_business_plan import create_business_plan_task

def create_crew():

    # Create the agents
    market_research_analyst = create_market_research_analyst()
    technologist = create_technologist()
    business_consultant = create_business_consultant()

    # Create the tasks and assign them to the agents
    analyze_market_demand = create_analyze_market_demand_task(market_research_analyst)
    analyze_technology_requirements = create_analyze_technology_requirements_task(technologist)
    create_business_plan = create_business_plan_task(business_consultant)

    # Create the crew
    crew = Crew(
        # The agents in the crew
        agents=[market_research_analyst, technologist, business_consultant],

        # The tasks that the crew will perform
        tasks=[analyze_market_demand, analyze_technology_requirements, create_business_plan],

        # Verbosity level of the crew
        verbose=2,

        # Run the tasks in sequential order - ensuring a systematic approach where the output of one task is the input of the next
        # https://docs.crewai.com/core-concepts/Processes/#sequential-process
        process=Process.sequential,
    )

    return crew

def run_crew():
    crew = create_crew()
    result = crew.kickoff()
    print(f"\nThe crew has completed their tasks:\n\n{result}")
