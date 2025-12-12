export const handler = async (event) => {
  try {
    //logging the incoming event for debugging
    console.log("Received event:", JSON.stringify(event, null, 2));

    // extracting values from the query parameter
    const transactionId =
      event?.queryStringParameters?.transactionId || event?.transactionId;
    const transactionType = event?.queryStringParameters?.transactionType;
    const transactionAmount = event?.queryStringParameters?.transactionAmount;

    // creating a response body
    const transactionResponse = {
      transactionId: transactionId,
      type: transactionType,
      amount: transactionAmount,
      message: "Hello from lambda by Tinashe github actions testing",
    };

    const response = {
      statusCode: 200,
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ transactionResponse }),
    };

    return response;
    
  } catch (error) {
    console.error("Error processing request", error);
    return {
      statusCode: 500,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ error: "Internal Server Error" }),
    };
  }
};
