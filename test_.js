import { handler } from "./index.js";


const event = {
  queryStringParameters: {
    transactionId: "12345",
    transactionType: "deposit",
    transactionAmount: "500",
  },
};

// printing the returned data in console 
handler(event).then((res) => {
  console.log("Lambda Output:");
  console.log(res);
});


const event2 = {
  queryStringParameters: {
    transactionId: "3434",
    transactionType: "credit",
    transactionAmount: "500",
  },
};

// printing the returned data in console 
handler(event2).then((res) => {
  console.log("Lambda Output:");
  console.log(res);
});
