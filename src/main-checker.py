import requests


def check_proxy(proxy):
    proxies = {
            'http': proxy,
            'https': proxy
            }
    #Need to add SSL certificate or ignore it and add proxy .strip
    #And correct input of proxy from user side
    answer = requests.get('https://instagram.com', proxies=proxy, verify=False)
    if answer.status_code == requests.code.ok:
        return 'Valid'
    else:
        return 'Invalid'
