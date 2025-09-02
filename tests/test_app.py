import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestSanchitRoute:
    """Test cases specifically for the /sanchit route."""
    
    def test_sanchit_route_exists(self, client):
        """Test that the /sanchit route exists and is accessible."""
        response = client.get('/sanchit')
        assert response.status_code == 200
    
    def test_sanchit_route_content(self, client):
        """Test that the /sanchit route returns the correct content."""
        response = client.get('/sanchit')
        assert response.data.decode('utf-8') == 'I am Sanchit'
    
    def test_sanchit_route_method_not_allowed(self, client):
        """Test that POST method is not allowed on /sanchit route."""
        response = client.post('/sanchit')
        assert response.status_code == 405
    
    def test_sanchit_route_put_method_not_allowed(self, client):
        """Test that PUT method is not allowed on /sanchit route."""
        response = client.put('/sanchit')
        assert response.status_code == 405

class TestHomeRoute:
    """Test cases for the home route."""
    
    def test_home_route_exists(self, client):
        """Test that the home route exists and is accessible."""
        response = client.get('/')
        assert response.status_code == 200
    
    def test_home_route_content(self, client):
        """Test that the home route returns the correct content."""
        response = client.get('/')
        assert response.data.decode('utf-8') == 'Hello, Flask Skeleton!'

class TestAboutRoute:
    """Test cases for the about route."""
    
    def test_about_route_exists(self, client):
        """Test that the /about route exists and is accessible."""
        response = client.get('/about')
        assert response.status_code == 200
    
    def test_about_route_content(self, client):
        """Test that the /about route returns the correct content."""
        response = client.get('/about')
        assert response.data.decode('utf-8') == 'This is the About page of the Flask Skeleton application.'

class TestGeneralAppBehavior:
    """Test general application behavior."""
    
    def test_404_for_nonexistent_route(self, client):
        """Test that nonexistent routes return 404."""
        response = client.get('/nonexistent')
        assert response.status_code == 404
    
    def test_app_has_correct_routes(self, client):
        """Test that all expected routes are accessible."""
        routes = ['/', '/sanchit', '/about']
        for route in routes:
            response = client.get(route)
            assert response.status_code == 200, f"Route {route} should be accessible"
