import requests

def uploadFile(file:str, url:str, maxDays=14, maxDownloads = None):
    print('Uploading...')
    headers = {
        'Max-Days': str(maxDays)
    }

    if maxDownloads is not None:
        headers['Max-Downloads'] = str(maxDownloads)

    with open(file, 'rb') as f:
        data = f.read()

    response = requests.put(url, headers = headers, data=data)

    return response.text

if __name__ == '__main__':
    uploadFile('hello.txt', 'https://transfer.sh/hello.txt')

    ## you can choose max days or max downloads

    uploadFile('hello.txt', 'https://transfer.sh/hello.xt', maxDays=30, maxDownloads=5)