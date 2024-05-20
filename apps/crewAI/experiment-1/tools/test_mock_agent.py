from unittest.mock import MagicMock, PropertyMock
from tools.mock_agent import create_mock_agent
from crewai import Agent

def test_create_mock_agent():
    # Create mock agent using the helper function
    mock_agent = create_mock_agent()

    # Assertions
    assert isinstance(mock_agent, MagicMock)
    assert isinstance(mock_agent, Agent)
    
    # Check for specific attributes
    assert hasattr(mock_agent, 'config')
    assert mock_agent.config == {}
    
    assert hasattr(mock_agent, 'verbose')
    assert mock_agent.verbose is True
    
    assert hasattr(mock_agent, 'max_rpm')
    assert mock_agent.max_rpm == 60
    
    assert hasattr(mock_agent, 'llm')
    assert isinstance(mock_agent.llm, MagicMock)
    
    assert hasattr(mock_agent, 'tools')
    assert isinstance(mock_agent.tools, MagicMock)
    
    assert hasattr(mock_agent, 'agent_executor')
    assert isinstance(mock_agent.agent_executor, MagicMock)
    
    assert hasattr(mock_agent, '_rpm_controller')
    assert isinstance(mock_agent._rpm_controller, PropertyMock)
    
    assert hasattr(mock_agent, '_token_process')
    assert isinstance(mock_agent._token_process, MagicMock)
