import responses

from api.config import REQRES_BASE_URL
from api.models.auth_models import LoginSuccessResponse, ErrorResponse

@responses.activate
def test_login_success_mock(reqres_client):
    responses.add(
        method=responses.POST,
        url=f"{REQRES_BASE_URL}/api/login",
        json={"token": "fake-token-123"},
        status=200,
        content_type="application/json",
    )

    resp = reqres_client.login(email="eve.holt@reqres.in", password="cityslicka")
    assert resp.status_code == 200
    model = LoginSuccessResponse.model_validate(resp.json)
    assert model.token == "fake-token-123"

@responses.activate
def test_login_missing_password_mock(reqres_client):
    responses.add(
        method=responses.POST,
        url=f"{REQRES_BASE_URL}/api/login",
        json={"error": "Missing password"},
        status=400,
        content_type="application/json",
    )
    
    resp = reqres_client.login_missing_password(email="peter@klaven")
    assert resp.status_code == 400
    model = ErrorResponse.model_validate(resp.json)
    assert model.error == "Missing password"