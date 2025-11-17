## 安装scanpy
```bash
conda create -y -p /pub/apps/biotools/scanpy scanpy python-igraph leidenalg

export PATH=/pub/apps/biotools/scanpy/bin:$PATH
```

- Error: ValueError: threshold is None and thus scrublet requires skimage, but skimage is not installed.
```bash
pip install scikit-image
```

