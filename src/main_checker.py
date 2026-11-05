import re
import requests


proxy_pattern = re.compile(
    r"(?:socks[45]|https?)://"
    r"(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
    r"(?:\.(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}"
    r":(?:[1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}"
    r"|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])"
)


def is_valid_proxy(proxy_add):
    return proxy_pattern.fullmatch(proxy_add) is not None


def check_proxy(proxy):
    proxy = proxy.strip()
    if not is_valid_proxy(proxy):
        return 'Incorrect format'

    proxies = {
            'http': proxy,
            'https': proxy
            }
    # Need to add SSL certificate or ignore it and add proxy .strip
    # And correct input of proxy from user side
    try:
        answer = requests.get(
                'https://instagram.com', 
                proxies=proxies, 
                verify=True, 
                timeout=10
        )
        if answer.status_code == requests.codes.ok:
            return 'Valid'
        else:
            return f'Invalid: {answer.status_code}'
    except requests.exceptions.ProxyError as error:
        return f'Invalid, proxy error: {error}'
    except requests.exceptions.Timeout:
        return 'Invalid, timeout'
    except requests.exceptions.ConnectionError as error:
        return f'Invalid, connection error: {error}'
