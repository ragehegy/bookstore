from uuid import uuid4

from django.db import models
from django.utils import timezone

from authentication.models import User

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    title = models.CharField(blank=False, unique=True, max_length=255)
    author = models.CharField(blank=False, max_length=255)
    date_published = models.DateTimeField()
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']
        permissions = [
             ('view_book_details', 'Can see all details/contents')
        ]

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='reviews')
    book = models.ForeignKey(Book, null=False, on_delete=models.CASCADE, related_name='reviews')
    content = models.CharField(blank=False, max_length=255)
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.content}'
    
    class Meta:
        ordering = ['created', 'updated_at']
        permissions = [
             ('write_review', 'Can write and submit a review'),
        ]