import pytest
from client.gist_client import GistClient

class TestGistCreation:
    @classmethod
    def setup_class(cls):
        cls.gist_client = GistClient()
        cls.created_gists = []

    def test_create_public_gist(self):
        description = "My Test Public Gist"
        files = {
            "test_file.txt": {
                "content": "Hello, world!"
            }
        }

        response = self.gist_client.create_gist(description, files, public=True)
        
        data = response.json()
        assert data['description'] == description
        assert data['public'] is True
        assert "test_file.txt" in data['files']

# Store the public gist ID for cleanup
        gist_id = data['id']
        self.__class__.created_gists.append(gist_id)
    
    def test_create_secret_gist(self):
        description = "My Test Secret Gist"
        files = {
            "test_file.txt": {
                "content": "Shush, world!"
            }
        }

        response = self.gist_client.create_gist(description, files, public=False)
        
        data = response.json()
        assert data['description'] == description
        assert data['public'] is False
        assert "test_file.txt" in data['files']

# Store the private gist ID for cleanup
        gist_id = data['id']
        self.__class__.created_gists.append(gist_id)

# Clean up created gists
    @classmethod
    def teardown_class(cls):

        for gist_id in cls.created_gists:
            cls.gist_client.delete_gist(gist_id)
