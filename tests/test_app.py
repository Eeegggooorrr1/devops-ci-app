"""Модульные тесты HTTP-интерфейса."""

import pytest

from app import create_app


@pytest.fixture()
def client():
    """Создаёт изолированный тестовый клиент Flask."""
    application = create_app()
    application.config.update(TESTING=True)

    with application.test_client() as test_client:
        yield test_client


def test_health(client):
    """Проверяет код и тело ответа health endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_index(client):
    """Проверяет основные сведения о службе."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {
        "service": "devops-ci-app",
        "version": "1.0.0",
        "status": "running",
    }
