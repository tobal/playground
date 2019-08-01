import pytest
import requests


@pytest.mark.vcr()
def test_vcr_example():
    response = requests.get('https://httpbin.org/')
    assert response.ok
    assert 'A simple HTTP Request &amp; Response Service.' in str(response.content)
