import pytest

from fastapi.testclient import TestClient

from app.main import app as fastapi_app


@pytest.fixture(scope="module")
def client():
    with TestClient(fastapi_app) as c:
        yield c


print('\n init test/conftest')  # noqa
