import pytest

from api.clients.reqres_client import ReqresClient
from api.config import REQRES_BASE_URL


@pytest.fixture
def reqres_client():
    return ReqresClient(base_url=REQRES_BASE_URL)
