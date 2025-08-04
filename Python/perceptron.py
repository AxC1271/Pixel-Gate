import torch
import torch.nn as nn
import torch.optim as optim

# define the Perceptron class model here
class Perceptron(nn.Module):
  def __init__(self, input_size):
    super(Perceptron, self).__init__()
    self.linear = nn.Linear(input_size, 1)

  def forward(self, x):
    return torch.sigmoid(self.linear(x))

# here we train the Perceptron model 

input_size = 1
model = Perceptron(input_size)

# binary cross entropy loss
criterion = nn.BCELoss()                           

# stochastic gradient descent with learning rate of 0.01
optimizer = optim.SGD(model.parameters(), lr=0.01) 

# training data

# training loop
