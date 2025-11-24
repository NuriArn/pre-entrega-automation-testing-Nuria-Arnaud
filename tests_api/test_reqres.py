import requests

BASE_URL = "https://6924e31882b59600d721b1fa.mockapi.io"
    
def test_get_users_page_2():
    # Crear un usuario temporal antes de consultar
    temp = requests.post(f"{BASE_URL}/users", json={"name": "Temporal"})
    assert temp.status_code == 201

    # Ahora sí: pedir la lista
    resp = requests.get(f"{BASE_URL}/users")
    assert resp.status_code == 200

    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0  # Ya hay al menos 1 usuario creado



def test_post_create_user():
    payload = {"name": "Nuria", "job": "QA Automation"}
    resp = requests.post(f"{BASE_URL}/users", json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert body["name"] == "Nuria"
    assert "id" in body


def test_delete_user():
    # Crear usuario temporal
    user = requests.post(f"{BASE_URL}/users", json={"name": "Temporal"})
    user_id = user.json()["id"]

    # Eliminar usuario
    resp = requests.delete(f"{BASE_URL}/users/{user_id}")
    assert resp.status_code in (200, 204)
