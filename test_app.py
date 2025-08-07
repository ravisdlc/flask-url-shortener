import pytest
from app import app  # Assuming your Flask app instance is named 'app' in app.py

@pytest.fixture
def client():
    # Set the Flask application to testing mode
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the / endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to the URL Shortener App!"}

def test_health_endpoint(client):
    """Test the /health endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "ok"}
