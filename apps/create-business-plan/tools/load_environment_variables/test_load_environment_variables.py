import os
from unittest.mock import patch
from tools.load_environment_variables.load_environment_variables import load_env_variables

def test_load_env_variables():
    with patch('tools.load_environment_variables.load_environment_variables.load_dotenv') as mock_load_dotenv:
        # Call the function
        load_env_variables()

        # Assert that load_dotenv was called once
        mock_load_dotenv.assert_called_once()

def test_env_variable_loaded():
    with patch('os.getenv') as mock_getenv:
        mock_getenv.return_value = 'fake_value'
        # Call the function to load .env variables
        load_env_variables()
        
        # Retrieve a specific variable to test if it was loaded
        result = os.getenv('FAKE_ENV_VARIABLE')

        # Assert that os.getenv was called with the variable name
        mock_getenv.assert_any_call('FAKE_ENV_VARIABLE')

        # Assert that the result is as expected
        assert result == 'fake_value'
