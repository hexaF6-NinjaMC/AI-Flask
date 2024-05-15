# AI-Flask

#### An AI served through the Flask microframework.

# This project provides an AI that's used as a chatbot in web applications.

## Data requests:

### How do I make requests in my application's HTML form?

  To use the API through your application's HTML form, you will need to utilize a Fetch() request through Javascript on the form's `<input>` element (assume `id="input-selector"` at the moment; adjust to your code).

  Use the URL
  ```
  https://ai-flask-m190.onrender.com/chatbot/predict
  ```
  in a Fetch() API POST request in your Javascript:
  ```javascript
  const textField = chatbox.querySelector("#input-selector");
  let text = textField.value;

  /**
   * BE SURE to add string checks here!
   * XSS and other malignant methods are bad!
   */

  fetch("https://ai-flask-m190.onrender.com/chatbot/predict", {
    method: "POST",
    body: JSON.stringify({ message: text }),
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
  })
  ```

  ### How are errors handled?

  If the URL is something the application doesn't access, the response will be something similar to a `404: Not Found` or other client-level conditional error. Other 400-level errors include `422: Unprocessable Entity` and `405: Method Not Allowed.`. The only server-level error response to be expected is `500: Internal Server Error`.

  ### How are the responses made available?

  The data from a successful request that the chatbot can formulate an "guesstmiated" answer with is returned through a Flask RestAPI in JSON format.

  Its appearance can be similar to the following examples below:
  - For a successful response ($\color{lime}{200}$-level success`):
      ```json
      {
        "answer": "This is the chatbot's answer as trained based on the text input. Yay! Show it to the user! Chances can be that the user needs to rephrase.",
        "status": 200 
      }
      ```

  - For an erroneously structured code implementation ($\color{orange}{400}$-level errors):
      ```json
      {
        "message": "Developer beware! The keyword \"message\" was not found in the JSON request object.",
        "status": 422
      }
      ```
      or
      ```json
      {
        "message": "Developer beware! The method for the URL was incorrect. should be a POST request.",
        "status": 405
      }
      ```
      or
      ```json
      {
        "message": "Developer beware! The URL request path was wrong.",
        "status": 404
      }
      ```
    
  - For server errors ($\color{yellow}{500}$-level errors):
      ```json
      {
        "message": "Good ol' internal server error: should be the only one. Contact the AI API server's owner!",
        "status": 500
      }
      ```
