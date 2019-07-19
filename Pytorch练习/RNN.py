import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as dsets
from torch.autograd import Variable

input_size = 28
sequence_length = 28
hidden_size = 128
num_layers = 2
num_classes = 10
batch_size = 100
num_epochs = 1
learning_rate = 0.01

train_datasets = dsets.MNIST(root='./data',
                             download=False,
                             train=True,
                             transform=transforms.ToTensor())
test_datasets = dsets.MNIST(root='./data',
                            download=False,
                            train=False,
                            transform=transforms.ToTensor())
train_loader = torch.utils.data.DataLoader(dataset=train_datasets,
                                           batch_size=batch_size,shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_datasets,
                                          batch_size=batch_size,
                                          shuffle=False)
class RNN(nn.Module):
    def __init__(self,input_size,hidden_size,num_layers,num_classes):
        super(RNN,self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        #https://pytorch.org/docs/master/nn.html?highlight=lstm#torch.nn.LSTM
        #参考官方文档
        self.lstm = nn.LSTM(input_size,hidden_size,num_layers,batch_first=True)
        self.fc = nn.Linear(hidden_size,num_classes)
    def forward(self, x):
        h0 = Variable(torch.zeros(self.num_layers, x.size(0), self.hidden_size))
        c0 = Variable(torch.zeros(self.num_layers, x.size(0), self.hidden_size))
        out,_ = self.lstm(x,(h0,c0))
        #选择最后一个时间点的output
        out = self.fc(out[:,-1,:])

        return out

rnn = RNN(input_size,hidden_size,num_layers,num_classes)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(rnn.parameters(),lr=learning_rate)

for epoch in range(num_epochs):
    for i,(images,labels) in enumerate(train_loader):
        images = Variable(images.view(-1,sequence_length,input_size))
        labels = Variable(labels)
        optimizer.zero_grad()
        outputs = rnn(images)
        loss = criterion(outputs,labels)
        loss.backward()
        optimizer.step()
        if (i+1) % 2 == 0:
            print('Epoch [%d/%d], Step [%d/%d], Loss: %.4f'
                  % (epoch + 1, num_epochs, i + 1, len(train_loader), loss.item()))

# Test the Model
correct = 0
total = 0
for images, labels in test_loader:
    images = Variable(images.view(-1, sequence_length, input_size))
    outputs = rnn(images)
    _, predicted = torch.max(outputs.data, 1)
    total += labels.size(0)
    correct += (predicted == labels).sum()

print('Test Accuracy of the model on the 10000 test images: %d %%' % (100 * correct / total))

# Save the Model
torch.save(rnn.state_dict(), 'rnn.pkl')
