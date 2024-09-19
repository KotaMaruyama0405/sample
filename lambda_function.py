def lambda_handler(event, context):

	return {
		"result": (event["first_num"] + event["second_num"])
	}
