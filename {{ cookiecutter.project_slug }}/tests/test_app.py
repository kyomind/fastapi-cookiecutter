"""Basic unit test for FastAPI app."""

from fastapi.testclient import TestClient


def test_root_endpoint(client: TestClient) -> None:
    """
    Test the root endpoint.

    Args:
        client: FastAPI test client fixture

    Returns:
        None
    """
    response = client.get("/")

    assert response.status_code == 200
