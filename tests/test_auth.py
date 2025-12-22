import responses

from api.config import REQRES_BASE_URL
from api.models.user_models import User
from api.models.user_models import SingleUserResponse, ListUsersResponse

@responses.activate
def test_get_user_mock(reqres_client):
    responses.add(
        method=responses.GET,
        url=f"{REQRES_BASE_URL}/api/users/2",
        json={
            "data": {
                "id": 2,
                "email": "janet.weaver@reqres.in",
                "first_name": "Janet",
                "last_name": "Weaver",
                "avatar": "https://reqres.in/img/faces/2-image.jpg",
            }
        },
        status=200,
        content_type="application/json",
    )

    resp = reqres_client.get_user(user_id=2)

    assert resp.status_code == 200
    payload = SingleUserResponse.model_validate(resp.json)
    assert payload.data.id == 2


@responses.activate
def test_list_users_mock(reqres_client):
    responses.add(
        method=responses.GET,
        url=f"{REQRES_BASE_URL}/api/users?page=1",
        json={
            "page": 1,
            "data": [
                {
                    "id": 1,
                    "email": "george.bluth@reqres.in",
                    "first_name": "George",
                    "last_name": "Bluth",
                    "avatar": "https://reqres.in/img/faces/1-image.jpg",
                }
            ],
        },
        status=200,
        content_type="application/json",
    )

    resp = reqres_client.list_users(page=1)

    assert resp.status_code == 200
    payload = ListUsersResponse.model_validate(resp.json)
    assert payload.page == 1
    assert len(payload.data) == 1
