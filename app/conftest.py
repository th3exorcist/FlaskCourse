import pytest
from app import iPudim

@apitest.fixture(schope="function")
def app():
    return create_app()