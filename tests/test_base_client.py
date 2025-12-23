import responses

from api.config import REQRES_BASE_URL

@responses.activate
def test_baseclient_sets_content_type_in_headers(reqres_client):
    responses.add(
        method=responses.GET,
        url=f"{REQRES_BASE_URL}/api/users/2",
        json={"data": {"id": 2, "email": "a@b.com", "first_name": "A", "last_name": "B", "avatar": "https://x.com/a.jpg"}},
        status=200,
        content_type="application/json",
    )

    resp = reqres_client.get_user(user_id=2)

    assert resp.status_code == 200
    assert "application/json" in resp.headers.get("Content-Type", "")
