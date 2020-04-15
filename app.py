import argparse

import numpy as np
import torch

from model.net import Net
from utils.data import tr_loader
from utils.image import img_save
from utils.kernels import custom_kernels


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('kernel', choices=list(custom_kernels.keys()))

    parser.print_help()
    return parser.parse_args()


if __name__ == '__main__':

    torch.manual_seed(1)
    np.random.seed(1)

    args = parse_args()

    net = Net(custom_kernels[args.kernel])

    with torch.no_grad():
        for img in tr_loader:
            out = net(img[0])
            img_save(out, args.kernel)
