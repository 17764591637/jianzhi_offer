import torch 
import torch.nn as nn 
import numpy as np 
from torch.autograd import Variable


theta1,theta2,bias = map(float,input().split())
theta = np.array([[theta1,theta2]],dtype=np.float32)
x_train = np.array([[1.1,6.1],
[2.1,4.1],
[3.1,2.1],
[4.1,7.1],
[5.1,9.1],
[2.3,4.2],
[3.3,2.1],
[4.1,7.3],
[5.3,9.1],
[2.1,4.1],
[3.1,2.1],
[4.1,7.1],
[5.1,9.1],
[2.3,4.1],
[3.3,2.1],
[4.1,7.3],
[5.3,9.1],
[2.1,4.1],
[3.1,2.1],
[4.1,7.1],
[5.1,9.1],
[2.3,4.1],
[3.3,2.1],
[4.1,7.3],
[5.3,9.1]
],dtype=np.float64)
b = np.array([bias])
y = np.dot(theta,x_train.T)[0] + b
x_train = torch.from_numpy(x_train)
y_train = torch.from_numpy(y).reshape(x_train.shape[0],1)

class Model(nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.layer = nn.Linear(2,1)

    def forward(self,x):
        out = self.layer(x)
        return out 

model = Model()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)
num_epochs = 4000

for epoch in range(num_epochs):
    inputs = Variable(x_train).float()
    target = Variable(y_train).float()
    # forward
    out = model(inputs)
    loss = criterion(out, target)
    # backward
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (epoch+1) % 2 == 0:
        print('Epoch[{}/{}], loss: {:.6f}'
              .format(epoch+1, num_epochs, loss.item()))
print(type(model.named_parameters()))
res = list(model.named_parameters())
print(res)