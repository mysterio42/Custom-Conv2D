```text
.
├── app.py
├── data
│   └── images
│       └── train
│           ├── sherlock.jpg
│           └── watson.jpg
├── figures
│   ├── kernels
│   │   ├── blur.png
│   │   ├── bottom-sobel.png
│   │   ├── emboss.png
│   │   ├── identity.png
│   │   ├── left-sobel.png
│   │   ├── outline.png
│   │   ├── right-sobel.png
│   │   ├── sharpen.png
│   │   └── top-sobel.png
│   └── outs
│       ├── blur-5bka4.png
│       ├── blur-sw9dc.png
│       ├── bottom-sobel-g3jqv.png
│       ├── bottom-sobel-locj6.png
│       ├── emboss-tdjiw.png
│       ├── emboss-x3q0q.png
│       ├── identity-ha7wv.png
│       ├── identity-xcg44.png
│       ├── left-sobel-tid8y.png
│       ├── left-sobel-z5qnf.png
│       ├── outline-bxnyo.png
│       ├── outline-sn5r6.png
│       ├── right-sobel-2s850.png
│       ├── right-sobel-uf4uv.png
│       ├── sharpen-lb09o.png
│       ├── sharpen-p4q1d.png
│       ├── top-sobel-0md2e.png
│       └── top-sobel-2myn4.png
├── model
│   ├── __init__.py
│   └── net.py
├── README.md
└── utils
    ├── data.py
    ├── image.py
    ├── __init__.py
    └── kernels.py

8 directories, 37 files

```

# Apply Custom Convolution Kernels
```shell script
python app.py 
```
```text
usage: app.py [-h]
              {outline,sharpen,emboss,blur,identity,left-sobel,right-sobel,bottom-sobel,top-sobel}

positional arguments:
  {outline,sharpen,emboss,blur,identity,left-sobel,right-sobel,bottom-sobel,top-sobel}

optional arguments:
  -h, --help            show this help message and exit
```
## Identity kernel
![identity.png](figures/kernels/identity.png)

```shell script
python app.py identity
```
```text
saved at figures/outs/identity-xcg44.png
saved at figures/outs/identity-ha7wv.png
```

### Sherlock
![identity-xcg44.png](figures/outs/identity-xcg44.png)

### Watson
![identity-ha7wv.png](figures/outs/identity-ha7wv.png)




## Outline kernel
![outline.png](figures/kernels/outline.png)

```shell script
python app.py outline
```
```text
saved at figures/outs/outline-sn5r6.png
saved at figures/outs/outline-bxnyo.png
```

### Sherlock
![outline-sn5r6.png](figures/outs/outline-sn5r6.png)

### Watson
![outline-bxnyo.png](figures/outs/outline-bxnyo.png)




## Sharpen kernel
![sharpen.png](figures/kernels/sharpen.png)

```shell script
python app.py sharpen
```
```text
saved at figures/outs/sharpen-lb09o.png
saved at figures/outs/sharpen-p4q1d.png
```

### Sherlock
![sharpen-lb09o.png](figures/outs/sharpen-lb09o.png)

### Watson
![sharpen-p4q1d.png](figures/outs/sharpen-p4q1d.png)




## Emboss kernel
![emboss.png](figures/kernels/emboss.png)

```shell script
python app.py emboss
```
```text
saved at figures/outs/emboss-x3q0q.png
saved at figures/outs/emboss-tdjiw.png
```

### Sherlock
![emboss-x3q0q.png](figures/outs/emboss-x3q0q.png)

### Watson
![emboss-tdjiw.png](figures/outs/emboss-tdjiw.png)




## Blur kernel
![blur.png](figures/kernels/blur.png)

```shell script
python app.py blur
```
```text
saved at figures/outs/blur-sw9dc.png
saved at figures/outs/blur-5bka4.png
```

### Sherlock
![blur-sw9dc.png](figures/outs/blur-sw9dc.png)

### Watson
![blur-5bka4.png](figures/outs/blur-5bka4.png)




## Left-Sobel kernel
![left-sobel.png](figures/kernels/left-sobel.png)

```shell script
python app.py left-sobel
```
```text
saved at figures/outs/left-sobel-tid8y.png
saved at figures/outs/left-sobel-z5qnf.png
```

### Sherlock
![left-sobel-tid8y.png](figures/outs/left-sobel-tid8y.png)

### Watson
![left-sobel-z5qnf.png](figures/outs/left-sobel-z5qnf.png)




## Right-Sobel kernel
![right-sobel.png](figures/kernels/right-sobel.png)

```shell script
python app.py right-sobel
```
```text
saved at figures/outs/right-sobel-uf4uv.png
saved at figures/outs/right-sobel-2s850.png
```

### Sherlock
![right-sobel-uf4uv.png](figures/outs/right-sobel-uf4uv.png)

### Watson
![right-sobel-2s850.png](figures/outs/right-sobel-2s850.png)




## Top-Sobel kernel
![top-sobel.png](figures/kernels/top-sobel.png)

```shell script
python app.py top-sobel
```
```text
saved at figures/outs/top-sobel-2myn4.png
saved at figures/outs/top-sobel-0md2e.png
```

### Sherlock
![top-sobel-2myn4.png](figures/outs/top-sobel-2myn4.png)

### Watson
![top-sobel-0md2e.png](figures/outs/top-sobel-0md2e.png)




## Bottom-Sobel kernel
![bottom-sobel.png](figures/kernels/bottom-sobel.png)

```shell script
python app.py bottom-sobel
```
```text
saved at figures/outs/bottom-sobel-g3jqv.png
saved at figures/outs/bottom-sobel-locj6.png
```

### Sherlock
![top-sobel-2myn4.png](figures/outs/bottom-sobel-g3jqv.png)

### Watson
![bottom-sobel-locj6.png](figures/outs/bottom-sobel-locj6.png)