"""
Arquivo de configuracao dos testes
"""
import os
import json
import pytest

with open('tests/mock/user.json', 'r', encoding='utf-8') as f:
    user_data = json.load(f)

MOCK_USER_EMAIL = user_data['email']
MOCK_USER_PASSWORD = user_data['password']

os.environ['SECRET_KEY'] = 'mock_secret_key'


@pytest.fixture
def mock_user():
    """
    Mock user
    """
    return user_data
