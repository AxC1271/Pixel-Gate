import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

# example data: pixel intensities and binary labels, you'll derive the data here

# create a dataset and data loader
dataset = TensorDataset(pixel_intensities, binary_labels)
data_loader = DataLoader(dataset, batch_size=1, shuffle=True)

# define the perceptron model
class Perceptron(nn.Module):
    def __init__(self):
        super(Perceptron, self).__init__()
        self.linear = nn.Linear(1, 1)
    
    def forward(self, x):
        return torch.sigmoid(self.linear(x))

# initialize model, loss function, and optimizer
model = Perceptron()
criterion = nn.BCELoss()  # Binary Cross-Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.1) # stochastic gradient descent

# training loop
for epoch in range(100):  # Number of epochs
    for inputs, labels in data_loader:
        optimizer.zero_grad()  # zero the gradients
        outputs = model(inputs)  # forward prop
        loss = criterion(outputs, labels)  # calculate loss
        loss.backward()  # backward pass
        optimizer.step()  # update weights

    if epoch % 10 == 0:
        print(f'Epoch [{epoch}/100], Loss: {loss.item():.4f}')

# derive trained weights and bias
weights = model.linear.weight.data.numpy()
bias = model.linear.bias.data.numpy()
print(f'Trained weights: {weights}, Bias: {bias}')
