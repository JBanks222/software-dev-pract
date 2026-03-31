"""
Jalen Banks
March 31,2026
RestAPIs unit testing
"""

# set-up a reusable compentent using pytest.fixture

import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True # enable testing mode in your flask app
    # create a Flask test client
    with app.test_client() as client:
        yield client
# test homepage
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200

# testing POST request
# CREATE ITEM

def test_create_item(client):
    response = client.post('/items', json={'name': 'Book', 'price': 10})
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['item']['name'] == 'Book'
    assert data['item']['price'] == 10

    # ------ test GET ALL ITEMS -------
    #read single item
def test_get_single_item(client):
    client.post('/items', json={'name': 'Laptop', 'price': 980})
    response = client.get('/items/2')
    assert response.status_code == 200
    assert response.get_json()['name'] == 'Laptop'
    

# read all items
def test_get_all_items(client):
    client.post('/items', json={'name': 'Phone', 'price': 500})
    response = client.get('/items')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 3  # we have 3 items in our in-memory database Book, Laptop, Phone)

    # testing put update item
def test_update_item(client):
    client.post('/items', json={'name': 'Tablet', 'price': 300})
    response = client.put('/items/3', json={'name': 'Tablet Pro', 'price': 350})
    assert response.status_code == 200
    data = response.get_json()
    assert data['item']['name'] == 'Tablet Pro'
    assert data['item']['price'] == 350

#------- testig delete item --------
def test_delete_item(client):
    response = client.delete('/items/1')
    assert response.status_code == 200
    get_all = client.get('/items').get_json()
    assert '1' not in get_all

    
