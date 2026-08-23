import requests


def check_proxy(proxy):
    proxy = proxy.strip()
    proxies = {
            'http': proxy,
            'https': proxy
            }
    #Need to add SSL certificate or ignore it and add proxy .strip
    #And correct input of proxy from user side
    try:
        answer = requests.get('https://instagram.com', proxies=proxies, verify=True, timeout=10)
    if answer.status_code == requests.codes.ok:
        return 'Valid'
    except requests.exceptions.ProxyError as error:
        return f'Invalid, proxy error: {error}'
    except requests.exceptions.Timeout:
        return 'Invalid, timeout'
    exccept requests.exceptions.ConnectionError as error:
        return f'Invalid, connection error: {error}'
    return 'Invalid'
