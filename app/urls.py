from django.urls import path

from . import views

urlpatterns = [
    path(
        "books",
        views.BooksView.as_view(
            actions={
                "get": "list",
                "post": "create",
            }
        ),
        name="books",
    ),
    # Book details/contents view
    path(
        "books/<pk>", views.BooksView.as_view(actions={"get": "retrieve"}), name="book"
    ),
    # Book reviews view
    path(
        "books/<pk>/reviews",
        views.ReviewsView.as_view(
            actions={
                "get": "retrieve",
                "post": "create",
            }
        ),
        name="reviews",
    ),
    path(
        "users",
        views.UsersView.as_view(
            actions={
                # 'get': 'list',
                "post": "create",
            }
        ),
        name="users",
    ),
    path(
        "users/<pk>",
        views.UsersView.as_view(
            actions={
                "get": "retrieve",
                "put": "update",
            }
        ),
        name="user",
    ),
]
