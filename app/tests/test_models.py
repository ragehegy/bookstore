from django.test import TestCase

from app.models import User, Book, Review

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='Test Book 1', author='Author 1', date_published='2024-10-16')
        
    def test_first_name_max_length(self):
        book = Book.objects.first()
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 255)

    def test_object_title_value(self):
        book = Book.objects.first()
        expected_object_title = f'{book.author} - {book.title}'
        self.assertEqual(str(book), expected_object_title)

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='testuser')
        user.set_password('123')
        user.save()
        
    def test_username_max_length(self):
        user = User.objects.get(username='testuser')
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 255)
        self.assertTrue(user.check_password('123'))

    def test_object_str_value(self):
        user = User.objects.first()
        expected_object_username = f'{user.username}'
        self.assertEqual(str(user), expected_object_username)


class ReviewModelTest(TestCase):
    fixtures = ['fixtures.json',]

    @classmethod
    def setUpTestData(cls):
        book = Book.objects.first()
        user = User.objects.first()
        Review.objects.create(
            user=user,
            book=book,
            content='test good review'
        )
        Review.objects.create(
            user=user,
            book=book,
            content='test bad review'
        )
        
    def test_username_max_length(self):
        user = Review.objects.first()
        max_length = user._meta.get_field('content').max_length
        self.assertEqual(max_length, 255)

    def test_object_str_value(self):
        review = Review.objects.first()
        expected_object_content = f'{review.content}'
        self.assertEqual(str(review), expected_object_content)
