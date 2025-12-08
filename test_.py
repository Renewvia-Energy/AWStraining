import json
from lambda_function import lambda_handler   # update filename if needed


def test_lambda_handler_success():
    # Mock event with query string parameters
    event = {
        "queryStringParameters": {
            "transactionId": "12345",
            "type": "deposit",
            "amount": "500"
        }
    }

    # Context will be none since its not being used in the lambda function
    response = lambda_handler(event, None)

    # Validate the structure of the response
    assert response["statusCode"] == 200
    assert response["headers"]["Content-Type"] == "application/json"

    # Parse the body to check values
    body = json.loads(response["body"])

    assert body["transactionId"] == "12345"
    assert body["type"] == "deposit"
    assert body["amount"] == "500"
    assert body["message"] == "Hello from lambda by Tinashe github actions testing"


def test_lambda_handler_missing_params():
    # event with missing params
    event = {
        "queryStringParameters": {}
    }

    response = lambda_handler(event, None)
    body = json.loads(response["body"])

    # Response still 200 no code validations. will add these later now we are just keeping things simple
    assert response["statusCode"] == 200

    # All fields should be None
    assert body["transactionId"] is None
    assert body["type"] is None
    assert body["amount"] is None
    assert body["message"] == "Hello from lambda by Tinashe github actions testing"
