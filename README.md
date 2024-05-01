# AI-Flask

#### An AI served through the Flask microframework.

## This project provides an AI that's used as a chatbot in web applications.

### Data requests:
__How are the responses made available?__
+ The data from a successful request that the chatbot can formulate an answer with is returned through a Flask RestAPI in JSON format.
  + Its appearance is as follows:

  ```json
  {
    "answer": "This is the answer. Show it to the user!",
    "status": 200
  }
  ```
+ To use the API in your application, you will need to utilize a Fetch() request through Javascript.
  + ~~Use the URL <> in your Javascript.~~

__How are errors handled?__

If the URL is something the application doesn't access, the response will be something similar to a `404: Not Found` or other client-level conditional error. Other 400-level errors include `422: Unprocessable Entity` and `405: Method Not Allowed.`. The only server-level error response to be expected is `500: Internal Server Error`.
