from unittest.mock import patch
from agents.technologist import create_technologist, ROLE, GOAL, BACKSTORY
from tools.normalize_whitespace import normalize_whitespace

def test_create_technologist():
    with patch('agents.technologist.Agent') as MockAgent:
        mock_agent_instance = MockAgent.return_value
        
        # Call the function
        agent = create_technologist()

        # Check if the Agent class was instantiated once with the correct arguments
        expected_role = normalize_whitespace(ROLE)
        actual_role = normalize_whitespace(MockAgent.call_args[1]['role'])
        
        expected_goal = normalize_whitespace(GOAL)
        actual_goal = normalize_whitespace(MockAgent.call_args[1]['goal'])

        expected_backstory = normalize_whitespace(BACKSTORY)
        actual_backstory = normalize_whitespace(MockAgent.call_args[1]['backstory'])
        
        assert expected_role == actual_role, f"Expected: {expected_role}, Actual: {actual_role}"
        assert expected_goal == actual_goal, f"Expected: {expected_goal}, Actual: {actual_goal}"
        assert expected_backstory == actual_backstory, f"Expected: {expected_backstory}, Actual: {actual_backstory}"
        
        MockAgent.assert_called_once_with(
            role=MockAgent.call_args[1]['role'],
            goal=MockAgent.call_args[1]['goal'],
            backstory=MockAgent.call_args[1]['backstory'],
            verbose=True,
            allow_delegation=True,
        )

        # Ensure the returned agent is the mock instance
        assert agent == mock_agent_instance
