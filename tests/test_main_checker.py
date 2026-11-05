import pytest
from src.main_checker import check_proxy, is_valid_proxy


@pytest.mark.parametrize(
        'proxy', 
        [
            'http://163.223.78.87:3127',
            'http://103.187.226.52:8082',
            'https://45.114.142.178:443',
            'https://138.199.35.215:9002',
            'socks4://24.249.199.12:4145',
            'socks4://174.77.111.196:4145',
            'socks5://208.102.51.6:58208',
            'socks5://69.61.200.104:36181'
        ],
)


def test_is_valid_proxy(proxy):
    assert is_valid_proxy(proxy) is True


@pytest.mark.parametrize(
        'proxy_add',
        [
            'http://163.223.78.87',
            'http://103.187.226.52/8082',
            'https://45.114.142:443',
            '138.199.35.215:9002',
            'socks://24.249.199.12:4145',
            'socks4://174.77.111.196:104145',
            'socks5://345.102.51.6:58208',
            'socks5:69.61.200.104:36181'
        ],
)


def test_is_valid_proxy(proxy_add):
    assert is_valid_proxy(proxy_add) is False


def test_check_proxy():
    assert check_proxy('') == 'Incorrect format'
    assert check_proxy(' ') == 'Incorrect format'
    assert check_proxy('1.1.1.1') == 'Incorrect format'
    assert check_proxy)'socks5://232.23.12.194') == 'Incorrect format'
