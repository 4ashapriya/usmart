import os
import pytest
from app.views import upload_csv
from app import app


@pytest.fixture
def client():
    # Set up the Flask app context
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_upload_csv_test1(client):
    # Load test data from test1.csv
    file_path = os.path.join(os.path.dirname(__file__), 'test/test1.csv')
    with open(file_path, 'rb') as file:
        data = {'file': (file, 'test1.csv')}
        response = client.post('/upload', data=data)

    # Assert the response
    assert response.status_code == 200
    assert response.json == {'message': 'Data uploaded successfully'}


def test_upload_csv_test2(client):
    # Load test data from test2.csv
    file_path = os.path.join(os.path.dirname(__file__), 'test/test2.csv')
    with open(file_path, 'rb') as file:
        data = {'file': (file, 'test2.csv')}
        response = client.post('/upload', data=data)

    # Assert the response
    assert response.status_code == 200
    assert response.json == {'message': 'Data uploaded successfully'}
