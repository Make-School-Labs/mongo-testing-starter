from app import app
from unittest import TestCase, main
from bson.objectid import ObjectId

class AppTests(TestCase): 
    """Run tests on the Songs App."""
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    @mock.patch("pymongo.collection.Collection.find")
    def test_show_songs(self, mock_find):
        

if __name__ == '__main__':
    main()