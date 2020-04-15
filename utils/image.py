import random
import string

import numpy as np
from matplotlib import pyplot as plt
from torchvision.utils import save_image

IMAGE_DIR = 'figures/outs/'


def generate_image_name(size=5):
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(size))


def img_save(tensor, kernel_name):
    img_name = IMAGE_DIR + kernel_name + '-' + generate_image_name(5) + '.png'
    save_image(tensor, img_name)
    print('saved at ' + img_name)


def img_show(tensor):
    '''
    :param tensor: 3-D
    :return:
    '''
    out = tensor[0].permute(1, 2, 0)
    out = (out.numpy() * 255).astype(np.uint8)
    plt.imshow(out)
    plt.show()


def imggray_show(tensor):
    out = tensor[0][0]
    plt.imshow(out, cmap='gray')
    plt.show()
