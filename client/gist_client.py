import requests
import logging
from config.config import Config

class GistClient:
    def __init__(self):
        self.base_url = f"{Config.GITHUB_API_URL}/gists"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"token {Config.GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json"
        })
# Method to create gists with public/private parameter
    def create_gist(self, description, files, public=True):
        payload = {
            "description": description,
            "public": public,
            "files": files
        }
# Try-Catch block raises HTTP error for bad responses
        try:
            response = self.session.post(self.base_url, json=payload)
            response.raise_for_status()  
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while updating the gist: {e}")

        return None
    
# Method to get gists
    def get_gist(self, gist_id):
        url = f"{self.base_url}/{gist_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status() 
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while updating the gist: {e}")
        return None
    
# Method to delete gists
    def delete_gist(self, gist_id):
        url = f"{self.base_url}/{gist_id}"
        try:
            response = self.session.delete(url)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while updating the gist: {e}")
        return None

