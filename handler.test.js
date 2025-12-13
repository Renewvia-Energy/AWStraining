import { handler } from "./index.js";

describe("Lambda Handler Tests", () => {

  test("handler returns correct success response", async () => {
    const event = {
      queryStringParameters: {
        transactionId: "12345",
        transactionType: "deposit",
        transactionAmount: "500",
      },
    };

    const response = await handler(event);
    const body = JSON.parse(response.body).transactionResponse;

    expect(response.statusCode).toBe(200);
    expect(response.headers["Content-Type"]).toBe("application/json");

    expect(body.transactionId).toBe("12345");
    expect(body.type).toBe("deposit");
    expect(body.amount).toBe("500");
    expect(body.message).toBe("Hello from lambda by Tinashe github actions testing");
  });

  test("handler works with missing params", async () => {
    const event = {
      queryStringParameters: {}
    };

    const response = await handler(event);
    const body = JSON.parse(response.body).transactionResponse;

    expect(response.statusCode).toBe(200);

    expect(body.transactionId).toBeUndefined();
    expect(body.type).toBeUndefined();
    expect(body.amount).toBeUndefined();
    expect(body.message).toBe("Hello from lambda by Tinashe github actions testing");
  });

});
