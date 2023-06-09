from app.models import User
from tests.utils import login


def test_auth(client):
    response = client.get("/login")
    assert response.status_code == 200
    response = client.get("/logout")
    assert response.status_code == 302


def test_login(client):
    user = User.query.filter_by(username="test").first()
    response = client.post(
        "/login", data=dict(user_id="test", password="test"), follow_redirects=True
    )
    assert b"Login Successful" in response.data

    response, _ = login(client, "wrong", "wrongpassword")
    assert b"Login Failed" in response.data

    response, _ = login(client, "test", "wrongpassword")
    assert b"Login Failed" in response.data


