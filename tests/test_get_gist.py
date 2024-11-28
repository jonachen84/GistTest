import pytest
from client.gist_client import GistClient

class TestGistRetrieval:
    @classmethod
    def setup_class(cls):
        cls.gist_client = GistClient()
        cls.created_gists = []

# Create a public gist
        description_public = "Public Gist for Retrieval Test"
        files_public = {
            "retrieve_public_test.txt": {
                "content": "This is a public test."
            }
        }
        response_public = cls.gist_client.create_gist(description_public, files_public, public=True)
        cls.public_gist_id = response_public.json()['id']
        cls.created_gists.append(cls.public_gist_id)

# Create a private gist
        description_private = "Private Gist for Retrieval Test"
        files_private = {
            "retrieve_private_test.txt": {
                "content": "This is a private test."
            }
        }
        response_private = cls.gist_client.create_gist(description_private, files_private, public=False)
        cls.private_gist_id = response_private.json()['id']
        cls.created_gists.append(cls.private_gist_id)

    def test_get_public_gist(self):
        response = self.gist_client.get_gist(self.public_gist_id)
        assert response.status_code == 200, "Failed to retrieve the public gist."

        data = response.json()
        assert data['id'] == self.public_gist_id
        assert data['public'] is True
        assert "retrieve_public_test.txt" in data['files']

    def test_get_private_gist(self):
        response = self.gist_client.get_gist(self.private_gist_id)
        assert response.status_code == 200, "Failed to retrieve the private gist."

        data = response.json()
        assert data['id'] == self.private_gist_id
        assert data['public'] is False
        assert "retrieve_private_test.txt" in data['files']

# Clean up created gists
    @classmethod
    def teardown_class(cls):
        
        for gist_id in cls.created_gists:
            cls.gist_client.delete_gist(gist_id)
