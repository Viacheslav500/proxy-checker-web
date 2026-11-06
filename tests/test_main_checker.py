import pytest
from unittest.mock import patch, Mock
from src.main_checker import check_proxy, is_valid_proxy


@pytest.mark.parametrize(
        'proxy_correct', 
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
def test_is_valid_proxy_on_valid_data(proxy_correct):
    assert is_valid_proxy(proxy_correct) is True


@pytest.mark.parametrize(
        'proxy_incorrect',
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
def test_is_valid_proxy_on_invalid_data(proxy_incorrect):
    assert is_valid_proxy(proxy_incorrect) is False


def test_check_proxy():
    fake_answer = Mock()
    fake_answer.status_code = 200
    with patch('src.main_checker.requests.get', return_value=fake_answer):
        result = check_proxy('http://127.0.0.1:8080')
    assert result == 'Valid'


@pytest.mark.parametrize(
        'status_code, expected',
            [
                (403, 'Invalid: 403'),
                (407, 'Invalid: 407'),
                (500, 'Invalid: 500'),
            ]
)
def test_check_proxy_other_answers(status_code, expected):
    fake_answer = Mock()
    fake_answer.status_code = status_code
    with patch('src.main_checker.requests.get', return_value=fake_answer):
        result = check_proxy('http://127.0.0.1:8080')
    assert result == expected
