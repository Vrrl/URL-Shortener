from src.domain.entities import Link

def test_should_save_new_valid_link(client):
    path = "/save"
    data = {
        "url": "teste.com"
    }
    
    assert 1 == 2

    # response = client.post(path + f"?url={data['url']}")
    # assert response.status_code == 200
    # assert "key" in response.json().keys()