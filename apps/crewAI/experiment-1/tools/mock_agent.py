from unittest.mock import MagicMock, PropertyMock
from crewai import Agent

def create_mock_agent():
    # Create a valid mock agent instance with necessary attributes
    mock_agent = MagicMock(spec=Agent)
    
    # Adding commonly expected attributes to the mock agent
    attrs = {
        'config': {},
        'verbose': True,
        'max_rpm': 60,
        'llm': MagicMock(),
        'tools': MagicMock(),
        'agent_executor': MagicMock(),
        '_rpm_controller': PropertyMock(),
        '_token_process': MagicMock()
    }
    
    for attr, value in attrs.items():
        setattr(mock_agent, attr, value)
    
    return mock_agent
