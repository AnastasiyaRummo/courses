import pytest
from api_client import YougileAPI, get_api_key
import config_local


@pytest.fixture(scope="session")
def api_client():

    token = get_api_key(
        config_local.LOGIN,
        config_local.PASSWORD,
        config_local.COMPANY_ID
    )
    return YougileAPI(config_local.BASE_URL, token)
