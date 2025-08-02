import requests


def get_api_key(login: str, password: str, company_id: str) -> str:
    url = "https://ru.yougile.com/api-v2/auth/keys"
    payload = {"login": login, "password": password, "companyId": company_id}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    return response.json().get("key")


class YougileAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str):
        url = f"{self.base_url}/api-v2/projects"
        payload = {"title": title}
        return requests.post(url, json=payload, headers=self.headers)

    def update_project(self, project_id: str, title: str):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {"title": title}
        return requests.put(url, json=payload, headers=self.headers)

    def get_project(self, project_id: str):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)
