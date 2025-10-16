import numpy as np

w = 1.0 # weight
x = 1.0 # input
b = 1.0 # bias
y = 1.0 # output
lr = 0.5 # learning rate

# sigmoid Function
def sigmoid(x):
  return 1 / (1 + np.exp(-x))

# loss function
def loss(yhat, y):
  return pow((yhat - y),2) /2

for epoch in range(0,100):
    # forward pass
    z = (w*x) + b
    yhat = a = sigmoid(z)
    # loss calculation
    L = loss(yhat, y)
    print(f"Loss = {L}")
    # back propagation
    dl_dw = (yhat - y)*yhat*(1 - yhat)*x
    dl_db = (yhat - y)*yhat*(1 - yhat)
    # updating weights and bias
    w = w-(lr*dl_dw)
    b = b-(lr*dl_db)
    print(f"New W = {w}, New b = {b}")
 