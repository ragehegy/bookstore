import random

from django.test import TestCase
from django.urls import reverse

from app.models import Book

class BooksViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_books = 13

        for book_id in range(number_of_books):
            Book.objects.create(
                title=f'Book {book_id}',
                author=f'Author {random.randint(1,6)}',
                date_published='2024-10-16'
            )

    def test_view_url_exists(self):
        response = self.client.get('/books')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('books'))
        self.assertEqual(response.status_code, 200)
