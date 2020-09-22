import json

	
def lambda_handler(event, context):
	# parsear
	a = event['queryStringParameters']['a']
	b = event['queryStringParameters']['b']
	op = event['queryStringParameters']['op']

	# operations
	res = 0
	if op == "add": res = int(a) + int(b)
	elif op == "sub": res = int(a) - int(b)
	elif op == "mul": res = int(a) * int(b)
	elif op == "div": res = int(a) / int(b)
	else: res = f"{op} is not a operation. Try 'add', 'sub', 'mul' or 'div'."

	# Resoponse
	Response = {}
	Response['a'] = a
	Response['b'] = b
	Response['result'] = res

	# http response
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(Response)

	return responseObject