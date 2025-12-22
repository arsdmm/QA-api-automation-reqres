from api.models.auth_models import LoginSuccessResponse


def test_login_success(reqres_client):
    response = reqres_client.login(
        email="eve.holt@reqres.in",
        password="cityslicka"
    )

    assert response.status_code == 200

    LoginSuccessResponse.model_validate(response.json)
