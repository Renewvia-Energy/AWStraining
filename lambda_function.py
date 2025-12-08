import json

print('Loading function')

def lambda_handler(event, context):
    # Extract query string parameters
    transactionId = event['queryStringParameters'].get('transactionId')
    transactionType = event['queryStringParameters'].get('type')
    transactionAmount = event['queryStringParameters'].get('amount')
    transactionUnits = event['queryStringParameters'].get('units')

    #unitcost = transactionAmount/transactionUnits

    print("transactionId=" + transactionId)
    print("transactionType=" + transactionType)
    print("transactionAmount=" + transactionAmount)

    # Construct the response body
    transactionResponse = {
        "transactionId": transactionId,
        "type": transactionType,
        "amount": transactionAmount,
        "message": "Hello from lambda by Tinashe github actions root"
    }

    # Construct HTTP response object
    responseObject = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(transactionResponse)
    }

    # Return the response object
    return responseObject

