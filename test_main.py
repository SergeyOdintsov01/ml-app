from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This model translation text"}

def test_translate_text():
    response = client.post("/translate/",
        json={"text": "Машина"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data["translation_text"] == "Car"

