import pytest
from server import app as _app


@pytest.fixture
def client(app):
    """Get a test client for your Flask app"""
    return app.test_client()


@pytest.fixture
def app():
    """Yield your app with its context set up and ready"""

    with _app.app_context():
        yield _app
