import json
import pytest
from app import create_app
from app.models import db, Fruit


@pytest.fixture
def app():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        db.create_all()
        fruits = [
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
        ]
        db.session.add_all(fruits)
        db.session.commit()
    yield app


@pytest.fixture
def client(app):
    return app.test_client()


def test_home_returnsDocumentationMessage(client):
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'message' in data


def test_getAllFruits_whenDatabaseHasFruits_returnsFruitsList(client):
    """
    Test fetching all fruits from the database.
    """
    response = client.get('/api/fruits')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]['name'] == 'Apple'


def test_addFruit_withValidData_returnsSuccessMessageAndFruitId(client):
    """
    Test adding a new fruit to the database.
    """
    new_fruit = {"name": "Orange", "quantity": 5, "variety": "Navel", "season": "Winter"}
    response = client.post('/api/fruits', json=new_fruit)
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data['message'] == 'Fruit added successfully'
    assert 'id' in data


def test_updateFruit_withValidId_updatesFruitSuccessfully(client):
    response = client.put('/api/fruits/1', json={"quantity": 25, "season": "Fall"})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'Fruit updated successfully'

    follow_up = client.get('/api/fruits')
    fruits = json.loads(follow_up.data)
    assert fruits[0]['quantity'] == 25
    assert fruits[0]['season'] == 'Fall'


def test_updateFruit_withMissingId_returnsNotFound(client):
    response = client.put('/api/fruits/999', json={"quantity": 4})
    data = json.loads(response.data)
    assert response.status_code == 404
    assert data['message'] == 'Fruit not found'


def test_deleteFruit_withValidId_removesFruit(client):
    response = client.delete('/api/fruits/1')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'Fruit deleted successfully'

    follow_up = client.get('/api/fruits')
    fruits = json.loads(follow_up.data)
    assert len(fruits) == 1


def test_deleteFruit_withMissingId_returnsNotFound(client):
    response = client.delete('/api/fruits/999')
    data = json.loads(response.data)
    assert response.status_code == 404
    assert data['message'] == 'Fruit not found'


def test_searchEndpoint_withMatchingCriteria_returnsFruitList(client):
    response = client.get('/api/fruits/search?name=Apple')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == 'Apple'


def test_searchEndpoint_withNoMatches_returnsMessage(client):
    response = client.get('/api/fruits/search?name=Pear')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == 'No fruits found matching the search criteria'

