import unittest
from flask import Flask
from app import create_app
class TestCreateApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    def test_app_instance(self):
        self.assertIsInstance(self.app, Flask)

    def test_sqlalchemy_database_uri(self):
        self.assertEqual(self.app.config['SQLALCHEMY_DATABASE_URI'], 'sqlite:///books.db')

    def test_swagger_config(self):
        self.assertIn('SWAGGER', self.app.config)
        self.assertEqual(self.app.config['SWAGGER']['title'], 'Book Review API')

    def test_app_blueprints(self):
        self.assertIn('api_bp', [bp.name for bp in self.app.blueprints.values()])

    # Optional: test a known route if available
    # def test_root_route(self):
    #     response = self.client.get('/')
    #     self.assertIn(response.status_code, (200, 404))  # Adjust based on your routes

if __name__ == '__main__':
    unittest.main()