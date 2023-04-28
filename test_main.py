from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_main_empty_message():
    # Ошибка при POST запросе без передачи файла
    response = client.post("/predict")
    assert response.status_code == 422
    
    
def test_read_predict_positive():
    response = client.post("/predict/",
        json={"text": "альфабанк"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data == 'альфабанк» (г. Москва) и «Сбербанк России» (г.'