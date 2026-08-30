from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_task():
    response = client.post("/tasks/", json={"title": "Test task", "priority": "high"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test task"
    assert data["status"] == "todo"


def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_complete_task():
    create_response = client.post("/tasks/", json={"title": "Task to complete"})
    task_id = create_response.json()["id"]
    response = client.patch(f"/tasks/{task_id}/complete")
    assert response.status_code == 200
    assert response.json()["status"] == "done"


def test_delete_task():
    create_response = client.post("/tasks/", json={"title": "Task to delete"})
    task_id = create_response.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204