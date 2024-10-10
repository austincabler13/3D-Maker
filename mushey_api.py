# mushey_api.py
import requests

class MusheyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.mushey.ai"

    def generate_3d_model(self, input_data):
        # Make API request to generate 3D model
        url = f"{self.base_url}/generate_3d_model"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.post(url, json=input_data, headers=headers)
        return response.json()