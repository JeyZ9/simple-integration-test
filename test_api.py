import requests

BASE_URL = "http://127.0.0.1:5000"

def test_create_user():
    response = requests.post(f"{BASE_URL}/users", json={'name': 'John Doe', 'email': 'john@example.com'})
    assert response.status_code == 201
    response_data = response.json()
    assert 'id' in response_data
    assert response_data['user']['name'] == 'John Doe'
    assert response_data['user']['email'] == 'john@example.com'

def test_get_user():
    # Create a user first
    response = requests.post(f"{BASE_URL}/users", json={'name': 'Jane Doe', 'email': 'jane@example.com'})
    user_id = response.json()['id']

    # Get the created user
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    response_data = response.json()
    assert response_data['id'] == user_id
    assert response_data['user']['name'] == 'Jane Doe'
    assert response_data['user']['email'] == 'jane@example.com'

def test_delete_user():
    # Create a user first
    response = requests.post(f"{BASE_URL}/users", json={'name': 'Mark Smith', 'email': 'mark@example.com'})
    user_id = response.json()['id']

    # Delete the created user
    response = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 204

    # Try to get the deleted user
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 404
    assert response.json()['error'] == 'User not found'