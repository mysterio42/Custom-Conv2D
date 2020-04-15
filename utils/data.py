from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import ImageFolder

trans = transforms.Compose([
    transforms.Grayscale(),
    transforms.ToTensor()
])

tr_set = ImageFolder('data/', transform=trans)
tr_loader = DataLoader(dataset=tr_set, batch_size=1)
