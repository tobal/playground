
import pytest
import vcr
import requests


def test_vcr_example():
    response = requests.get('https://httpbin.org/')
    assert response == 'asdf'
