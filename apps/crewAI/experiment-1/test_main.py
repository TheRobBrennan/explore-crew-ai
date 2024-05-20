from unittest.mock import patch
from main import main

@patch('main.load_env_variables')
@patch('main.run_crew')
def test_main(mock_run_crew, mock_load_env_variables):
    # Call the main function
    main()

    # Assertions
    mock_load_env_variables.assert_called_once()
    mock_run_crew.assert_called_once()
