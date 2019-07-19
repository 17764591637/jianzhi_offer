import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torchvision.datasets as dsets
from torch.autograd import Variable

batch_size = 100
learning_rate = 0.01
num_epochs = 1

train_datasets = dsets.MNIST(root='./data',
                             train=True,
                             transform=transforms.ToTensor(),
                             download=False)
test_datasets = dsets.MNIST(root='./data',
                            train=False,
                            transform=transforms.ToTensor(),
                            download=False)
train_loader = torch.utils.data.DataLoader(dataset=train_datasets,
                                           batch_size=batch_size,
                                           shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_datasets,
                                           batch_size=batch_size,
                                           shuffle=False)
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=5, padding=2),# 输入图像大小（1*28*28）
            nn.BatchNorm2d(16),#（16*28*28）
            nn.ReLU(),
            nn.MaxPool2d(2))#（16*14*14）
        self.layer2 = nn.Sequential(
            nn.Conv2d(16, 32, kernel_size=5, padding=2),
            nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2))
        self.fc = nn.Linear(7*7*32, 10)

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = x.view(x.size(0), -1)
        out = self.fc(x)
        return out

cnn = CNN()
if torch.cuda.is_available():
    cnn.cuda()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(cnn.parameters(),lr=learning_rate)

for epoch in range(num_epochs):
    for i,(images,labels) in enumerate(train_loader):
        if torch.cuda.is_available():
            images = Variable(images).cuda()
            labels = Variable(labels).cuda()
        else:
            images = Variable(images)
            labels = Variable(labels)

        optimizer.zero_grad()
        outputs = cnn(images)
        loss = criterion(outputs,labels)
        loss.backward()
        optimizer.step()

        if (i+1) % 10 == 0:
            print('Epoch:[%d/%d],Step:[%d/%d],Loss:%.4f' % (
            epoch + 1, num_epochs, i + 1, len(train_datasets) // batch_size, loss.item()))

cnn.eval()
correct = 0
total = 0
for j,(images,labels) in enumerate(test_loader):
    if torch.cuda.is_available():
        images = Variable(images).cuda()
    else:
        images = Variable(images)
    outputs = cnn(images)
    _,predicted = torch.max(outputs.data,1)
    total += labels.shape[0]
    correct += (predicted==labels).sum()

print('Accuracy of the model on the 10000 test images: %d %%' % (100 * correct / total))

torch.save(cnn.state_dict(),'cnn_model.pkl')