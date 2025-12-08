import json

print('Loading function')

def lambda_handler(event, context):
    # Extract query string parameters
    transactionId = event['queryStringParameters'].get('transactionId')
    transactionType = event['queryStringParameters'].get('type')
    transactionAmount = event['queryStringParameters'].get('amount')
    #transactionUnits = event['queryStringParameters'].get('units')

    #unitcost = transactionAmount/transactionUnits

    print(f"transactionId= {transactionId}" )
    print(f"transactionType= {transactionType}")
    print(f"transactionAmount= {transactionAmount}")

    # the response body that will be sent when the request is a success in the response object
    transactionResponse = {
        "transactionId": transactionId,
        "type": transactionType,
        "amount": transactionAmount,
        "message": "Hello from lambda by Tinashe github actions testing"
    }

    # HTTP response object
    responseObject = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(transactionResponse)
    }


    return responseObject

   


