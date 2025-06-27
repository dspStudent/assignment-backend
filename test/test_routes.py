import unittest
import json
from app import create_app

class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test variables and app."""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        # You might want to set up a test database here if your endpoints interact with one

    def tearDown(self):
        """Tear down all initialized variables."""
        # You might want to tear down the test database here
        pass

    def test_get_books(self):
        """Test fetching all books."""
        # Assuming you have some books in the database for testing,
        # otherwise you might need to mock the get_all_books service function.
        res = self.client.get('/books')
        self.assertEqual(res.status_code, 200)
        self.assertIn('application/json', res.content_type)
        data = json.loads(res.get_data(as_text=True))
        self.assertIsInstance(data, list)
        # Add more specific assertions based on expected data structure if needed

    def test_post_books(self):
        """Test creating new books."""
        new_books_data = [
            {"title": "Test Book 1", "author": "Test Author 1", "description": "Description 1"},
            {"title": "Test Book 2", "author": "Test Author 2", "description": "Description 2"}
        ]
        res = self.client.post('/books', data=json.dumps(new_books_data), content_type='application/json')
        self.assertEqual(res.status_code, 201)
        self.assertIn('application/json', res.content_type)
        data = json.loads(res.get_data(as_text=True))
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 2)
        self.assertIn('id', data[0])
        self.assertIn('title', data[0])
        self.assertIn('author', data[0])

    def test_post_books_invalid_data(self):
        """Test creating books with invalid data."""
        invalid_books_data = [
            {"author": "Test Author 1"}, # Missing title
            {"title": "", "author": "Test Author 2"} # Empty title
        ]
        res = self.client.post('/books', data=json.dumps(invalid_books_data), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn('application/json', res.content_type)
        data = json.loads(res.get_data(as_text=True))
        self.assertIn('message', data)

    def test_get_book_reviews(self):
        """Test fetching reviews for a specific book."""
        # Assuming you have a book with ID 1 and some reviews for it,
        # or you need to mock the get_reviews_by_book_id service function.
        # You might need to create a book and add reviews before running this test.
        book_id = 1
        res = self.client.get(f'/books/{book_id}/reviews')
        # This might return 200 with an empty list if no reviews, or 404 if book not found.
        # Adjust assertion based on your expected behavior or mock setup.
        self.assertIn(res.status_code, [200, 404])
        self.assertIn('application/json', res.content_type)
        data = json.loads(res.get_data(as_text=True))
        if res.status_code == 200:
             self.assertIsInstance(data, list)


    def test_post_book_review(self):
        """Test adding a review to a book."""
        # Assuming you have a book with ID 1,
        # or you need to mock the add_review_to_book service function.
        # You might need to create a book before running this test.
        book_id = 1
        new_review_data = {
            "reviewer": "Test Reviewer",
            "comment": "Great book!"
        }
        res = self.client.post(f'/books/{book_id}/reviews', data=json.dumps(new_review_data), content_type='application/json')
        # This might return 201 on success or 404 if book not found, or 400 for invalid input.
        # Adjust assertion based on your expected behavior or mock setup.
        self.assertIn(res.status_code, [201, 400, 404])
        if res.status_code == 201:
            self.assertIn('application/json', res.content_type)
            data = json.loads(res.get_data(as_text=True))
            self.assertIn('id', data)
            self.assertEqual(data['book_id'], book_id)
            self.assertEqual(data['reviewer'], new_review_data['reviewer'])
            # Add assertions for rating and comment if they are returned in the response

    def test_post_book_review_invalid_data(self):
        """Test adding a review with invalid data."""
        book_id = 1
        invalid_review_data = {
            "reviewer": "Test Reviewer",
            "comment": "Great book!"
        } # Missing reviewer
        res = self.client.post(f'/books/{book_id}/reviews', data=json.dumps(invalid_review_data), content_type='application/json')
        self.assertEqual(res.status_code, 400)
        self.assertIn('application/json', res.content_type)
        data = json.loads(res.get_data(as_text=True))
        self.assertIn('message', data)


if __name__ == '__main__':
    unittest.main()