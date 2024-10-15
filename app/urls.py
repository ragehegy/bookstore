from django.urls import path

from . import views

urlpatterns = [
    path('books', views.BooksView.as_view(actions={'get': 'list'}), name='books'),
    path('books/<pk>', views.BooksView.as_view(actions={'get': 'retrieve'}), name='books'),
    path('users', views.UsersView.as_view(actions={'get': 'list'}), name='users'),
    path('reviews/<book_id>', views.ReviewsView.as_view(actions={'get': 'list'}), name='reviews'),
]