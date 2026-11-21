def test_home_page_opens(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"TaskFlow" in response.data

def test_create_task(client):
    response = client.post("/tasks", data={
        "title": "Separar pedidos",
        "description": "Conferir os pedidos do dia",
        "priority": "Alta",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Separar pedidos".encode() in response.data

def test_task_requires_title(client):
    response = client.post("/tasks", data={"title": "   "}, follow_redirects=True)
    assert "Informe um título".encode() in response.data

def test_update_task_status(client):
    client.post("/tasks", data={"title": "Organizar estoque"})
    response = client.post("/tasks/1/update", data={
        "title": "Organizar estoque",
        "description": "",
        "status": "Concluída",
        "priority": "Média",
    }, follow_redirects=True)
    assert response.status_code == 200
    assert "Concluída".encode() in response.data

def test_delete_task(client):
    client.post("/tasks", data={"title": "Tarefa temporária"})
    response = client.post("/tasks/1/delete", follow_redirects=True)
    assert response.status_code == 200
    assert "Tarefa temporária".encode() not in response.data
