import os
import requests


def check():
    url = os.getenv('INPUT_URL')
    status = int(os.getenv('INPUT_STATUS'))
    method = os.getenv('INPUT_METHOD')
    assert method in ['get', 'post', 'put']
    user = os.getenv('INPUT_USER')
    password = os.getenv('INPUT_PASSWORD')

    if user:
        auth = (user, password)
    else:
        auth = None

    response = getattr(requests, method)(url=url, auth=auth)
    if response.status_code != status:
        print(f'* {url} - error: expected [{status}], actual [{response.status_code}]')
        exit(1)
    else:
        print(f'* {url} - success')


if __name__ == '__main__':
    check()
