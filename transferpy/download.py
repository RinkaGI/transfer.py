import requests

def downloadFile(url:str, file:str):
    response = requests.get(str(url))

    with open(file, 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    downloadFile('https://transfer.sh/2olwuBElm6/hello.txt', 'hello.txt')