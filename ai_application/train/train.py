"""Trains the Chatbot interface"""
# pylint: disable=invalid-name
# pylint: disable=too-many-locals
# pylint: disable=too-many-statements
import json
from pathlib import Path

import numpy as np
import torch
from torch import nn
from torch.utils.data import DataLoader, Dataset
from ai_application.model import model
from ai_application.nltk_utils import nltk_utils

def train_chatbot():
    """Train the Chatbot interface"""
    file_path = Path("ai_application/intents.json")
    if file_path.is_file():
        # File exists! We can train!
        with open("ai_application/intents.json", mode='r', encoding='utf-8') as f:
            intents = json.load(f)

        all_words = []
        tags = []
        xy = []

        # loop through each sentence in our intents patterns
        for intent in intents['intents']:
            tag = intent['tag']
            # add to tag list
            tags.append(tag)
            for pattern in intent['patterns']:
                # tokenize each word in the sentence
                w = nltk_utils.tokenize(pattern)
                # add to our words list
                all_words.extend(w)
                # add to xy pair
                xy.append((w, tag))

        # stem and lower each word
        ignore_words = ['?', '.', '!']
        all_words = [nltk_utils.stem(w) for w in all_words if w not in ignore_words]
        # remove duplicates and sort
        all_words = sorted(set(all_words))
        tags = sorted(set(tags))

        # create training data
        x_train = []
        y_train = []
        for (pattern_sentence, tag) in xy:
            # X: bag of words for each pattern_sentence
            bag = nltk_utils.bag_of_words(pattern_sentence, all_words)
            x_train.append(bag)
            # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
            label = tags.index(tag)
            y_train.append(label)

        x_train = np.array(x_train)
        y_train = np.array(y_train)

        # Hyper-parameters
        num_epochs = 1000
        batch_size = 10
        learning_rate = 0.01
        input_size = len(x_train[0])
        hidden_size = 10
        output_size = len(tags)

        class ChatDataset(Dataset):
            """The Chat dataset"""
            def __init__(self):
                self.n_samples = len(x_train)
                self.x_data = x_train
                self.y_data = y_train

            # support indexing such that dataset[i] can be used to get i-th sample
            def __getitem__(self, index):
                return self.x_data[index], self.y_data[index]

            # we can call len(dataset) to return the size
            def __len__(self):
                return self.n_samples

        dataset = ChatDataset()
        train_loader = DataLoader(
            dataset=dataset,
            batch_size=batch_size,
            shuffle=True,
            num_workers=0
        )

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        net_model = model.NeuralNet(input_size, hidden_size, output_size).to(device)

        # Loss and optimizer
        criterion = nn.CrossEntropyLoss()
        optimizer = torch.optim.Adam(net_model.parameters(), lr=learning_rate)

        # Train the model
        for epoch in range(num_epochs):
            for (words, labels) in train_loader:
                words = words.to(device)
                labels = labels.to(dtype=torch.long).to(device)
                # Forward pass
                # pylint: disable-next=not-callable
                outputs = net_model(words)
                # if y would be one-hot, we must apply
                # labels = torch.max(labels, 1)[1]
                loss = criterion(outputs, labels)
                # Backward and optimize
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
            if (epoch+1) % 100 == 0:
                print (f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.6f}')


        print(f'final loss: {loss.item():.6f}')

        data = {
            "model_state": net_model.state_dict(),
            "input_size": input_size,
            "hidden_size": hidden_size,
            "output_size": output_size,
            "all_words": all_words,
            "tags": tags
        }

        FILE = "data.pth"
        torch.save(data, FILE)

        print(f"Training complete. Model training data saved to \"{FILE}\".")
    else:
        print("intents.json file not found.")

if __name__ == "__main__":
    train_chatbot()
