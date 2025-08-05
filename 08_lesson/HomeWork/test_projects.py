def test_create_project_positive(api_client):
    create_response = api_client.create_project(title="Autotest Project")
    assert create_response.status_code in (200, 201)
    project_id = create_response.json()["id"]
    assert project_id is not None

    get_response = api_client.get_project(project_id)
    assert get_response.status_code == 200
    project_data = get_response.json()
    assert project_data["title"] == "Autotest Project"


def test_create_project_negative_no_name(api_client):
    response = api_client.create_project(title="")
    assert response.status_code in (400, 422)


def test_update_project_positive(api_client):
    create_resp = api_client.create_project(title="Project To Update")
    project_id = create_resp.json()["id"]

    update_resp = api_client.update_project(
        project_id, title="Updated Project")
    assert update_resp.status_code == 200

    get_resp = api_client.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Updated Project"


def test_update_project_negative_invalid_id(api_client):
    response = api_client.update_project(project_id="invalid_id", title="Test")
    assert response.status_code == 404


def test_get_project_positive(api_client):
    create_resp = api_client.create_project(title="Project For Get")
    project_id = create_resp.json()["id"]

    get_resp = api_client.get_project(project_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == project_id


def test_get_project_negative_not_found(api_client):
    response = api_client.get_project(project_id="non_existent_id")
    assert response.status_code == 404
