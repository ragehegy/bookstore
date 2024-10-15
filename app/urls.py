from django.urls import path

from . import views

urlpatterns = [
    path('books', views.BooksView.as_view(actions={
        'get': 'list',
        'post': 'create',
    }), name='books'),
    
    path('books/<pk>', views.BooksView.as_view(actions={'get': 'retrieve'}), name='book'),
    
    path('books/<pk>/reviews', views.ReviewsView.as_view(actions={
        'get': 'list',
        'post': 'create',
    }), name='reviews'),
   
    path('users', views.UsersView.as_view(actions={
        'get': 'list',
        'post': 'create',
    }), name='users'),
]