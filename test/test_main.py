# https://fastapi.tiangolo.com/em/tutorial/testing/

#import unittest
#from fastapi.testclient import TestClient
#from main import app

#from typing import List
#from schemas.geocache import CacheDocument
#from schemas.document import Document
"""
class TestApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_post_addDocuments(self):
        mock_document = Mock(spec=Document)
        #mock_obj.get_message.return_value =
        response = self.client.post("/addDocuments", json={"document": List[mock_document]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message" : "Documentos procesados correctamente"})

    def test_post_addcache(self):
        mock_cacheDocument = Mock(spec=CacheDocument)
        response = self.client.post("/addcache", json={"document": mock_cacheDocument})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"msg": "Añadido correctamente"})

    def test_get_checkcache(self):
        response = self.client.get("/checkcache")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 0)

if __name__ == "__main__":
    unittest.main()
"""

from fastapi.testclient import TestClient

from .src.main import app

fake_db = {
    "foo": {"id": "foo", "title": "Foo", "description": "There goes my hero"},
    "bar": {"id": "bar", "title": "Bar", "description": "The bartenders"},
}

client = TestClient(app)

def test_read_main():
    # Mock de la sesión de la base de datos
    mock_db = app.SessionLocal.return_value
    mock_db.execute.return_value = [(1,)]
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
