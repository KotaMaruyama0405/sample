import pytest
from lambda_function import lambda_handler

def test_lambda_handler():
	event = {
		"first_num": 3,
		"second_num": 2
	}

	result = lambda_handler(event, {})
	assert (result["result"] == 5)
