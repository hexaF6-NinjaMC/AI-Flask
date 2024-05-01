# AI-Flask

#### An AI served through the Flask microframework.

## This project provides an AI that's used as a chatbot in web applications.

### Data requests:
__How are the responses made available?__
+ The data is returned through a Flask RestAPI in JSON format.
  + Its appearance is as follows:

  <pre json>
  {
    "answer": ${\color{orange}<i>str</i>}$,
    "status": ${\color{orange}<i>int</i>}$
  }
  </pre>
+ To use the API in your application, you will need to utilize a Fetch() request through Javascript.
