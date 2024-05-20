from unittest.mock import patch, MagicMock
from crew.create_crew import create_crew, run_crew
from crewai import Crew

@patch('crew.create_crew.create_market_research_analyst')
@patch('crew.create_crew.create_technologist')
@patch('crew.create_crew.create_business_consultant')
@patch('crew.create_crew.create_analyze_market_demand_task')
@patch('crew.create_crew.create_analyze_technology_requirements_task')
@patch('crew.create_crew.create_business_plan_task')
@patch('crew.create_crew.Crew', autospec=True)
def test_create_crew(mock_Crew, mock_create_business_plan_task, mock_create_analyze_technology_requirements_task,
                     mock_create_analyze_market_demand_task, mock_create_business_consultant, 
                     mock_create_technologist, mock_create_market_research_analyst):

    # Mock return values for the agent creation functions
    mock_market_research_analyst = MagicMock()
    mock_technologist = MagicMock()
    mock_business_consultant = MagicMock()

    mock_create_market_research_analyst.return_value = mock_market_research_analyst
    mock_create_technologist.return_value = mock_technologist
    mock_create_business_consultant.return_value = mock_business_consultant

    # Mock return values for the task creation functions
    mock_analyze_market_demand_task = MagicMock()
    mock_analyze_technology_requirements_task = MagicMock()
    mock_create_business_plan_task = MagicMock()

    mock_create_analyze_market_demand_task.return_value = mock_analyze_market_demand_task
    mock_create_analyze_technology_requirements_task.return_value = mock_analyze_technology_requirements_task
    mock_create_business_plan_task.return_value = mock_create_business_plan_task

    # Create the crew
    crew = create_crew()

    # Assert that the crew was created with the correct agents, tasks, and process
    assert isinstance(crew, Crew)  # Ensure crew is an instance of the Crew class

@patch('crew.create_crew.create_crew')
@patch('crew.create_crew.Crew.kickoff', autospec=True)
def test_run_crew(mock_kickoff, mock_create_crew):
    mock_crew_instance = MagicMock()
    mock_create_crew.return_value = mock_crew_instance
    mock_crew_instance.kickoff.return_value = "Mocked Result"
    
    run_crew()
    
    mock_create_crew.assert_called_once()
    mock_crew_instance.kickoff.assert_called_once()
    assert mock_crew_instance.kickoff.return_value == "Mocked Result"
