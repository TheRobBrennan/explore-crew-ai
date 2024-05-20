from tasks.analyze_market_demand import create_analyze_market_demand_task, DESCRIPTION, EXPECTED_OUTPUT
from crewai import Task
from tools.mock_agent import create_mock_agent

def test_create_analyze_market_demand_task():
    # Create a mock agent using the helper function
    mock_agent = create_mock_agent()

    # Create task
    task = create_analyze_market_demand_task(mock_agent)

    # Assertions
    assert isinstance(task, Task)
    assert task.description == DESCRIPTION
    assert task.agent == mock_agent
    assert task.expected_output == EXPECTED_OUTPUT
