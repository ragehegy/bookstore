from uuid import uuid4

from django.db import models
from django.utils import timezone

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    title = models.CharField(blank=False, unique=True, max_length=255)
    author = models.CharField(blank=False, unique=True, max_length=255)
    date_published = models.DateTimeField()
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']
        verbose_name = 'User'

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    username = models.CharField("username", blank=False, unique=True, max_length=255)
    visible = models.BooleanField(default=True)
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.username}'

    class Meta:
        ordering = ['username', 'created']

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='reviews')
    content = models.CharField(blank=False, max_length=255)
    created = models.DateTimeField(editable=False, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.content}'
    
    class Meta:
            ordering = ['created', 'updated_at']