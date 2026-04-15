import pytest
from app import create_app
from app.models import Fruit, db


@pytest.fixture
def test_app():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    with app.app_context():
        db.create_all()
        fruits = [
            Fruit(name="Apple", quantity=10, variety="Gala", season="Winter"),
            Fruit(name="Banana", quantity=20, variety="Cavendish", season="All"),
            Fruit(name="Apple", quantity=15, variety="Fuji", season="Winter"),
            Fruit(name="Orange", quantity=8, variety="Navel", season="Summer"),
        ]
        db.session.add_all(fruits)
        db.session.commit()
    yield app


def test_searchByName_withExistingFruitName_returnsFruitsWithName(test_app):
    """
    Test the search functionality by name in the Fruit model.
    Verifies that the search method returns the correct fruits when searching by name.
    """
    with test_app.app_context():
        results = Fruit.search(name="Apple")
        assert len(results) == 2
        assert all(fruit.name == "Apple" for fruit in results)


def test_searchByVariety_withExistingVariety_returnsMatchingFruit(test_app):
    with test_app.app_context():
        results = Fruit.search(variety="Gala")
        assert len(results) == 1
        assert results[0].variety == "Gala"


def test_searchBySeason_withExistingSeason_returnsSeasonMatches(test_app):
    with test_app.app_context():
        results = Fruit.search(season="Winter")
        assert len(results) == 2
        assert all(fruit.season == "Winter" for fruit in results)


def test_searchByMinQuantity_withThreshold_returnsLargerQuantities(test_app):
    with test_app.app_context():
        results = Fruit.search(min_quantity=15)
        assert len(results) == 2
        assert all(fruit.quantity >= 15 for fruit in results)


def test_searchByMaxQuantity_withThreshold_returnsSmallerQuantities(test_app):
    with test_app.app_context():
        results = Fruit.search(max_quantity=10)
        assert len(results) == 2
        assert all(fruit.quantity <= 10 for fruit in results)


def test_search_withNoMatches_returnsEmptyList(test_app):
    with test_app.app_context():
        results = Fruit.search(name="Pear")
        assert results == []

