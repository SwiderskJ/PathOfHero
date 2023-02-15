
def test_home_page(client):
    """
    Tests if home page is opening and checks if status code is OK (200)
    """
    response = client.get('/')
    assert response.status_code == 200

