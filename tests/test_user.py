from app.models import User
from tests.utils import login


def test_create(client):
    response = client.post(
        "/user/create",
        data=dict(username="test", password="test"),
        follow_redirects=True,
    )
    assert b"User already exist" in response.data
