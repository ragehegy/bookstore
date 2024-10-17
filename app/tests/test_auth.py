from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class LoanedBookInstancesByUserListViewTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        user.set_password("123")
        user.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.post(reverse("books"))
        self.assertEquals(response.status_code, 401)

    def test_logged_in_uses_correct_template(self):
        login = self.client.post(
            reverse("login"), data={"username": "testuser", "password": "123"}
        )
        self.assertEqual(login.status_code, 200)

        tokens = login.data.get("tokens", None)
        self.assertIsNotNone(tokens)
        access = tokens.get("access", None)
        self.assertIsNotNone(access)

        headers = {"Authorization": f"Bearer {access}"}
        response = self.client.post(
            reverse("books"),
            data={
                "title": "Book Test",
                "author": "Author 1",
                "date_published": "2024-10-16T23:39:13.325Z",
            },
            headers=headers,
        )
        self.assertEqual(response.status_code, 201)
