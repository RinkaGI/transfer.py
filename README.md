
# transfer.py

Use transfer.sh with python





![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

Maybe u can donate me on Bitcoin : 
bc1q6kyex89x9ppqw0kww9qfrtfrta6sdhnvgjz87r
## Installation

Install transfer.py with pip

```bash
    pip install transferpy
```
    
## Usage/Examples

Download a file:
```py
downloadFile('https://transfer.sh/2olwuBElm6/hello.txt', 'hello.txt')
```

Upload a file (simple way):
```py
uploadFile('hello.txt', 'https://transfer.sh/hello.txt')
```

Upload a file (complete way):
```py
uploadFile('hello.txt', 'https://transfer.sh/hello.xt', maxDays=30, maxDownloads=5)
```