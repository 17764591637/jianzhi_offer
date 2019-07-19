import torch
import torch.nn as nn
import torchvision.datasets as dsets
from torch.autograd import Variable
import torchvision.transforms as transforms

input_size = 784
batch_size = 100
num_epochs = 10
learning_rate = 0.001

train_datasets = dsets.MNIST(root='./data',
                            train=True,
                            download=False,
                            transform=transforms.ToTensor())
test_datasets = dsets.MNIST(root='./data',
                            train=False,
                            download=False,
                            transform=transforms.ToTensor())
train_loader = torch.utils.data.DataLoader(dataset=train_datasets,batch_size=batch_size,shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_datasets,batch_size=batch_size,shuffle=False)

class feedforward_neural_network(nn.Module):
    def __init__(self,input_size,hidden,num_classes):
        super(feedforward_neural_network, self).__init__()
        self.linear = nn.Linear(input_size,hidden)
        self.r = nn.ReLU()
        self.out = nn.Linear(hidden,num_classes)

    def forward(self, x):
        x = self.linear(x)
        x = self.r(x)
        out = self.out(x)

        return out

if torch.cuda.is_available():
    model = feedforward_neural_network(input_size=input_size,hidden=50,num_classes=10).cuda()
else:
    model = feedforward_neural_network(input_size=input_size,hidden=50,num_classes=10)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=learning_rate)

for epoch in range(num_epochs):
    for i ,(images,labels) in enumerate(train_loader):
        if torch.cuda.is_available():
            images = Variable(images.view(-1,28*28)).cuda()
            labels = Variable(labels).cuda()
        else:
            images = Variable(images.view(-1,28*28))
            labels = Variable(labels)
        outputs = model(images)
        optimizer.zero_grad()
        loss = criterion(outputs,labels)
        loss.backward()
        optimizer.step()

        if (i+1) % 10 == 0:
            print('Epoch:[%d/%d],Step:[%d/%d],Loss:%.4f' % (epoch+1,num_epochs,i+1,len(train_datasets)//batch_size,loss.item()))

correct = 0
total = 0
for j,(images,labels) in enumerate(test_loader):
    if torch.cuda.is_available():
        images = Variable(images.view(-1,28*28)).cuda()
        labels = Variable(labels).cuda()
    else:
        images = Variable(images.view(-1,28*28))
    outputs = model(images)
    _,predictes = torch.max(outputs.data,1)
    total += labels.shape[0]
    correct += (predictes==labels).sum()
print('Accuracy of the model on the 10000 test images: %d %%' % (100 * correct / total))

torch.save(model.state_dict(),'model3.pkl')