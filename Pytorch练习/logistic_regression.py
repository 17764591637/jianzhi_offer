import torch
import torch.nn as nn
from torch.autograd import Variable
import torchvision.datasets as dsets
import torchvision.transforms as transforms

input_size = 784
num_classes = 10
num_epoch = 1
batch_size = 100
learning_rate = 0.01

train_dataset = dsets.MNIST(root='./data',
                            train=True,
                            transform=transforms.ToTensor(),
                            download=True)

test_dataset = dsets.MNIST(root='./data',
                           train=False,
                           transform=transforms.ToTensor())

train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = torch.utils.data.DataLoader(dataset=test_dataset,
                                          batch_size=batch_size,
                                          shuffle=False)

class Logistic_regression(nn.Module):
    def __init__(self,input_size,hidden,num_classes):
        super(Logistic_regression,self).__init__()
        self.linear1 = nn.Linear(input_size,hidden)
        self.linear2 = nn.Linear(hidden,num_classes)

    def forward(self, x):
        x = self.linear1(x)
        out = self.linear2(x)

        return out

if torch.cuda.is_available():
    model = Logistic_regression(input_size=input_size,hidden=50,num_classes=num_classes).cuda()
else:
    model = Logistic_regression(input_size=input_size,hidden=50,num_classes=num_classes)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(),lr=learning_rate)

for epoch in range(num_epoch):
    for i, (images, labels) in enumerate(train_loader):
        if torch.cuda.is_available():
            images = Variable(images.view(-1, 28 * 28)).cuda()
            labels = Variable(labels).cuda()
        else:
            images = Variable(images.view(-1, 28 * 28))
            labels = Variable(labels)

        # Forward + Backward + Optimize
        optimizer.zero_grad()
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)#返回每一行中最大值的那个元素，且返回其索引,即predicted
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        if (i + 1) % 100 == 0:
            print('Epoch: [%d/%d], Step: [%d/%d], Loss: %.4f'
                  % (epoch + 1, num_epoch, i + 1, len(train_dataset) // batch_size, loss.item()))
correct = 0
total = 0
for i, (images, labels) in enumerate(test_loader):
    if torch.cuda.is_available():
        images = Variable(images.view(-1, 28 * 28)).cuda()
        labels = Variable(labels).cuda()
    else:
        images = Variable(images.view(-1, 28 * 28))
        labels = Variable(labels)
    outputs = model(images)
    _, predicted = torch.max(outputs.data, 1)
    total += labels.shape[0]
    correct += (predicted == labels).sum()

print('Accuracy of the model on the 10000 test images: %d %%' % (100 * correct / total))

torch.save(model.state_dict(),'model2.pkl')