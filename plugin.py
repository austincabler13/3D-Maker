import requests

class MeshyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.meshy.ai"

    def generate_3d_model(self, input_data):
        url = f"{self.base_url}/generate_3d_model"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        try:
            response = requests.post(url, json=input_data, headers=headers)
            if response.status_code == 200:
                return response.json()
            else:
                return {"status": "error", "message": response.text}
        except requests.exceptions.RequestException as e:
            return {"status": "error", "message": str(e)}
