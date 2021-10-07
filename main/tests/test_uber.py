from fastapi.testclient import TestClient
import json
import pytest
from main import app



def test_login_200():
    client = TestClient(app)
    result = client.post(
        '/uber/login',
        json={
            "email": "pierre@palenca.com",
            "password": "MyPwdChingon123",
        }
    )
    assert result.status_code == 200

def test_login_401():
    client = TestClient(app)
    result = client.post(
        '/uber/login',
        json={
            "email": "pierre@palenca.com1",
            "password": "MyPwdChingon123",
        }
    )
    assert result.status_code == 401

def test_profile_200():
    client = TestClient(app)
    result = client.post(
        '/uber/get-profile',
        json={
            "access_token": "cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F5",
            "password": "MyPwdChingon123",
        }
    )
    assert result.status_code == 200


def test_profile_401():
    client = TestClient(app)
    result = client.post(
        '/uber/get-profile',
        json={
            "access_token": "cTV0aWFuQ2NqaURGRE82UmZXNVBpdTRxakx3V1F51",
            "password": "MyPwdChingon123",
        }
    )
    assert result.status_code == 401