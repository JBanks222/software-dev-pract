# Jalen Banks
# May 5th, 2026
#lab 19: unit test for verifying authentication in a flask-sqlite app
import os
import sqlite3
import pytest 
from app import app


#-------
# TEST HOME REDIRECT    
#-------
def test_home_redirect():
    response = app.test_client().get('/')
    assert response.status_code == 302
    assert '/login' in response.location # response.location = a proper redirect to URL location, in this case, the login page.
#-------
# TEST DATABASE SETUP
#-------

TEST_DB = 'test_flask_auth.db'

def init_test_db():
    #simulate a databse connection
    conn = sqlite3.connect(TEST_DB)
    cursor = conn.cursor()

    # Create a template table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# create a mock database to run the app.py file\
@pytest.fixture
def client(monkeypatch):
    #override database to use test database
    def test_get_db():
        conn = sqlite3.connect(TEST_DB)
        conn.row_factory = sqlite3.Row
        return conn
    #match the mock db
    from app import get_db
    monkeypatch.setattr('app.get_db', test_get_db)
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test_secret'

    #call function to run the mock database
    init_test_db()

     #create an instance of the Flask test client
    with app.test_client() as client:
        # yield means returns the client and after all tests are finished the 
        yield client