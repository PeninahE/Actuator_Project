from typing import List

import requests


class ServiceCaller:
    json_response : str
    service_url : str


    def __init__(self, service_url: str):
        self.service_url = service_url


    # def __str__(self):
    def call_service(self) -> str:
        response = requests.get("http://127.0.0.1:8000/pyctuator/health")
        self.json_response = response.text
        return self.json_response
