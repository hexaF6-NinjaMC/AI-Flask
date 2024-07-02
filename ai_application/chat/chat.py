"""Sets up Chatbot chat functionality"""
import json
import random
import torch
from ai_application.model.model import NeuralNet
from ai_application.nltk_utils.nltk_utils import bag_of_words, tokenize

# pylint: disable-next=too-many-locals
def get_response(msg: str) -> str:
    """
    Initializes application setup, and also re-initializes intents file with
    the new intents received from the POST upload. Then, it uses the loaded model
    to generate a response based on the given message.

    :param str msg: the user's input message
    :return: a response based on the given message `msg`
    :rtype: str.
    """

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load the saved intents even after POST upload
    intents_file = "ai_application/intents.json"

    with open(intents_file, mode='r', encoding='utf-8') as json_data:
        intents = json.load(json_data)

    file = "ai_application/data.pth"
    data = torch.load(file)

    input_size = data["input_size"]
    hidden_size = data["hidden_size"]
    output_size = data["output_size"]
    all_words = data['all_words']
    tags = data['tags']
    model_state = data["model_state"]

    # pylint: disable-next=invalid-name
    model = NeuralNet(input_size, hidden_size, output_size).to(device)
    model.load_state_dict(model_state)
    model.eval()

    sentence = tokenize(msg)
    x = bag_of_words(sentence, all_words)
    x = x.reshape(1, x.shape[0])
    x = torch.from_numpy(x).to(device)

    # pylint: disable-next=not-callable
    output = model(x)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    return "I do not understand... Can you rephrase that? I may be better capable to serve you."

# Use this code to run the chatbot from the command line (dev)
if __name__ == "__main__":
    print("Let's chat! (type 'quit' to exit)")
    while True:
        userInput = input("You: ")
        if userInput == "quit":
            break
        resp = get_response(userInput)
        print(resp)
