import torch

custom_kernels = {
    'outline': torch.Tensor([[[
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1],
    ]]
    ]),
    'sharpen': torch.Tensor([[[
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0],
    ]]
    ]),
    'emboss': torch.Tensor([[[
        [-2, -1, 0],
        [-1, 1, 1],
        [0, 1, 2],
    ]]
    ]),
    'blur': 1 / 16 * torch.Tensor([[[
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1],
    ]]
    ]),
    'identity': torch.Tensor([[[
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]]
    ]),
    'left-sobel': torch.Tensor([[[
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1],
    ]]
    ]),
    'right-sobel': torch.Tensor([[[
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1],
    ]]
    ]),
    'bottom-sobel': torch.Tensor([[[
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1],
    ]]
    ]),
    'top-sobel': torch.Tensor([[[
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1],
    ]]
    ])
}
