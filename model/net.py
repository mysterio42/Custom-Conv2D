import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

    def __init__(self, kernel):
        super(Net, self).__init__()
        self.kernel = kernel
        self.relu = nn.ReLU()
        self.maxpooling = nn.MaxPool2d(kernel_size=2)

    def forward(self, x):
        out = F.conv2d(x, self.kernel)
        out = self.relu(out)
        out = self.maxpooling(out)
        return out
