from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_register_user():
    mock_user = {
        "state": 1,
        "msg": "success",
        "data": {
            "exito": True,
            "mensaje": "USUARIO_REGISTRADO"
        }
    }
    response = client.post(
        "/User/Register",
        json={
            "name": "User",
            "last_name": "Test",
            "email": "test@gmail.com",
            "password": "password",
            "phone": "999999999"
        }
    )
    assert response.status_code == 201
    assert response.json() == mock_user

def test_get_user():
    mock_user = {
        "state": 1,
        "msg": "success",
        "data": {
            "user": {
                "name": "Joel",
                "last_name": "Sigüenza",
                "email": "siguenzajoel10@gmail.com",
                "phone": "921018664",
                "id_user": 1
            }
        }
    }
    response = client.get("/User/1")
    assert response.status_code == 200
    assert response.json() == mock_user