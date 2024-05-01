class Chatbox {
  constructor() {
    this.args = {
      openButton: document.querySelector(".chatbox__button"),
      chatBox: document.querySelector(".chatbox__support"),
      sendButton: document.querySelector(".send__button")
    }
    this.state = false;
    this.messages = [];
  }

  display() {
    const {openButton, chatBox, sendButton} = this.args;
    openButton.addEventListener("click", () => this.toggleState(chatBox))
    sendButton.addEventListener("click", () => this.onSendButton(chatBox))
    const node = chatBox.querySelector("input");
    node.addEventListener("keyup", ({key}) => {
      if (key === "Enter") {
        this.onSendButton(chatBox)
      }
    })
  }

  toggleState(chatbox) {
    this.state = !this.state;
    // show or hide the box
    chatbox.classList.toggle("chatbox--active")
  }

  onSendButton(chatbox) {
    const textField = chatbox.querySelector("input");
    let text = textField.value
    if (text === "") {
      return;
    }

    let msg1 = {
      name: "User",
      message: text
    }
    this.messages.push(msg1);

    fetch("http://127.0.0.1:5000/chatbot/predict", {
      method: "POST",
      body: JSON.stringify({ message: text }),
      mode: "cors",
      headers: {
        "Content-Type": "application/json"
      },
    })
    .then(r => r.json())
    .then(r => {
      let msg2 = { name: "Algee", message: r.answer };
      this.messages.push(msg2);
      this.updateChatText(chatbox)
      textField.value = ""
    })
    .then(() => {
      this.messages = [];
    })
    .catch((error) => {
      console.error("Error: ", error);
      this.updateChatText(chatbox)
      textField.value = ""
    });
  }

  updateChatText(chatbox) {
    const chatMessage = chatbox.querySelector(".chatbox__messages");
    const chat_html = document.querySelector(".chatbox__content");
    this.messages.slice().forEach((item) => {
      let convo_html = document.createElement("div");
      if (item.name === "Algee") {
        convo_html.textContent = `Algee: ${item.message}`
        convo_html.classList.add("messages__item", "messages__item--visitor")
      } else {
        convo_html.textContent = `You: ${item.message}`
        convo_html.classList.add("messages__item", "messages__item--operator")
      }
      chat_html.insertAdjacentElement("beforeend", convo_html);
      chatMessage.appendChild(chat_html);
    });
  }
}

const chatbox = new Chatbox();
chatbox.display();